import atexit
from dataclasses import dataclass
import inspect
import json
import logging
import os
from threading import Condition
import time
from typing import Callable, List, Optional, Tuple
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from ..utils.async_loop import run_async

logger = logging.getLogger(__name__)

BROWSER_USE_CONCURRENCY_ENV = "BROWSER_USE_CONCURRENCY"
BROWSER_USE_BILLING_URL = "https://api.browser-use.com/api/v2/billing/account"
FALLBACK_BROWSER_USE_CONCURRENCY = 3
BROWSER_USE_SESSION_TTL_SECONDS = 10 * 60

__condition = Condition()
__records: List["BrowserRecord"] = []
__active_slots = 0
__queue_limit: Optional[int] = None
__cloud_limit_key: Optional[str] = None
__cloud_limit: Optional[int] = None
__cloud_limit_checked = False


@dataclass(frozen=True)
class BrowserPoolKey:
    api_key: str
    user_data_dir: str
    headless: bool
    extra_args: Tuple[str, ...]


@dataclass
class BrowserRecord:
    browser: object
    key: BrowserPoolKey
    created_at: float
    in_use: bool


def _positive_int(value: object, source: str) -> Optional[int]:
    try:
        limit = int(str(value).strip())
    except (TypeError, ValueError):
        logger.warning("Invalid %s value: %r", source, value)
        return None

    if limit < 0:
        logger.warning("%s must be zero or greater; got %s", source, limit)
        return None
    if limit == 0:
        return None
    return limit


def _configured_limit() -> Optional[int]:
    raw = os.getenv(BROWSER_USE_CONCURRENCY_ENV)
    if raw is not None and raw.strip():
        return _positive_int(raw, BROWSER_USE_CONCURRENCY_ENV)

    try:
        from ..context import ctx

        return _positive_int(
            ctx.config.crawler.browser_use_concurrency,
            "crawler.browser_use_concurrency",
        )
    except Exception:
        logger.exception("Failed to read BrowserUse concurrency config")
        return None


def _fetch_cloud_limit(api_key: str) -> Optional[int]:
    request = Request(
        BROWSER_USE_BILLING_URL,
        headers={"X-Browser-Use-API-Key": api_key},
        method="GET",
    )
    try:
        with urlopen(request, timeout=10) as response:
            payload = response.read()
    except HTTPError as e:
        logger.info("BrowserUse Cloud limit lookup failed with HTTP %s", e.code)
        return None
    except (TimeoutError, URLError, OSError) as e:
        logger.info("BrowserUse Cloud limit lookup failed: %s", e)
        return None

    try:
        data = json.loads(payload)
    except json.JSONDecodeError as e:
        logger.info("BrowserUse Cloud limit lookup returned invalid JSON: %s", e)
        return None

    if not isinstance(data, dict):
        logger.info("BrowserUse Cloud limit lookup returned an unexpected response")
        return None

    return _positive_int(data.get("rateLimit"), "BrowserUse Cloud rateLimit")


def _cloud_limit_from_api(api_key: str) -> Optional[int]:
    global __cloud_limit, __cloud_limit_checked, __cloud_limit_key

    with __condition:
        if __cloud_limit_checked and __cloud_limit_key == api_key:
            return __cloud_limit

    limit = _fetch_cloud_limit(api_key)

    with __condition:
        __cloud_limit_key = api_key
        __cloud_limit = limit
        __cloud_limit_checked = True
    return limit


def resolve_browser_use_concurrency(api_key: Optional[str] = None) -> int:
    configured = _configured_limit()
    if configured is not None:
        return configured

    if api_key:
        cloud_limit = _cloud_limit_from_api(api_key)
        if cloud_limit is not None:
            return cloud_limit

    return FALLBACK_BROWSER_USE_CONCURRENCY


def _stop_browser(browser: object, timeout: Optional[float] = None) -> None:
    try:
        result = getattr(browser, "stop")()
        if inspect.isawaitable(result):
            run_async(result, timeout=timeout)
    except Exception:
        logger.exception("Failed to stop browser instance")


def _find_record(browser: object) -> Optional[BrowserRecord]:
    for record in __records:
        if record.browser is browser:
            return record
    return None


def _evict_expired_idle_locked() -> List[BrowserRecord]:
    global __records, __active_slots

    now = time.monotonic()
    expired: List[BrowserRecord] = []
    kept: List[BrowserRecord] = []
    for record in __records:
        if not record.in_use and now - record.created_at >= BROWSER_USE_SESSION_TTL_SECONDS:
            expired.append(record)
        else:
            kept.append(record)
    __records = kept
    __active_slots -= len(expired)
    return expired


def acquire_browser(
    key: BrowserPoolKey,
    create_browser: Callable[[], object],
    api_key: Optional[str] = None,
) -> object:
    global __active_slots, __queue_limit

    limit = resolve_browser_use_concurrency(api_key)
    with __condition:
        if __queue_limit != limit:
            logger.info("BrowserUse concurrency limit: %s", limit)
            __queue_limit = limit
            __condition.notify_all()

        while True:
            expired = _evict_expired_idle_locked()
            now = time.monotonic()
            for record in __records:
                if (
                    not record.in_use
                    and record.key == key
                    and now - record.created_at < BROWSER_USE_SESSION_TTL_SECONDS
                ):
                    record.in_use = True
                    return record.browser

            if __queue_limit is None or __active_slots < __queue_limit:
                __active_slots += 1
                break

            __condition.wait()

    for record in expired:
        _stop_browser(record.browser, timeout=10)

    try:
        browser = create_browser()
    except Exception:
        with __condition:
            __active_slots -= 1
            __condition.notify_all()
        raise

    with __condition:
        __records.append(
            BrowserRecord(
                browser=browser,
                key=key,
                created_at=time.monotonic(),
                in_use=True,
            )
        )
        return browser


def release_browser(
    browser: object,
    *,
    reusable: bool = True,
    timeout: Optional[float] = None,
) -> None:
    global __records, __active_slots

    with __condition:
        record = _find_record(browser)
        if record is None:
            return

        age = time.monotonic() - record.created_at
        if reusable and age < BROWSER_USE_SESSION_TTL_SECONDS:
            record.in_use = False
            __condition.notify_all()
            return

        __records = [r for r in __records if r is not record]
        __active_slots -= 1
        __condition.notify_all()

    _stop_browser(record.browser, timeout=timeout)


def check_active(browser: Optional[object]) -> bool:
    with __condition:
        return browser is not None and _find_record(browser) is not None


def cleanup_drivers() -> None:
    global __records, __active_slots

    with __condition:
        records = list(__records)
        __records = []
        __active_slots = 0
        __condition.notify_all()

    for record in records:
        _stop_browser(record.browser, timeout=10)


atexit.register(cleanup_drivers)
