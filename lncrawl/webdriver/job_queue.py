import atexit
import inspect
import json
import logging
import os
from threading import Condition
from typing import List, Optional
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from ..utils.async_loop import run_async

logger = logging.getLogger(__name__)

BROWSER_USE_CONCURRENCY_ENV = "BROWSER_USE_CONCURRENCY"
BROWSER_USE_BILLING_URL = "https://api.browser-use.com/api/v2/billing/account"
FALLBACK_BROWSER_USE_CONCURRENCY = 3

__condition = Condition()
__open_browsers: List[object] = []
__active_slots = 0
__queue_limit: Optional[int] = None
__cloud_limit_key: Optional[str] = None
__cloud_limit: Optional[int] = None
__cloud_limit_checked = False


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


def acquire_queue(api_key: Optional[str] = None) -> None:
    global __active_slots, __queue_limit

    limit = resolve_browser_use_concurrency(api_key)
    with __condition:
        if __queue_limit != limit:
            logger.info("BrowserUse concurrency limit: %s", limit)
            __queue_limit = limit
            __condition.notify_all()

        while __queue_limit is not None and __active_slots >= __queue_limit:
            __condition.wait()

        __active_slots += 1


def _find_browser_index(browser: object) -> Optional[int]:
    for index, open_browser in enumerate(__open_browsers):
        if open_browser is browser:
            return index
    return None


def _release_queue_slot() -> None:
    global __active_slots

    with __condition:
        if __active_slots <= 0:
            logger.warning("BrowserUse queue slot released while none were active")
            return

        __active_slots -= 1
        __condition.notify()


def register_browser(browser: object) -> None:
    with __condition:
        if _find_browser_index(browser) is None:
            __open_browsers.append(browser)


def release_browser(browser: object) -> None:
    with __condition:
        index = _find_browser_index(browser)
        if index is None:
            return

        __open_browsers.pop(index)

    _release_queue_slot()
    logger.info("Destroyed browser instance")


def check_active(browser: Optional[object]) -> bool:
    with __condition:
        return browser is not None and _find_browser_index(browser) is not None


def cleanup_drivers() -> None:
    with __condition:
        browsers = list(__open_browsers)

    for browser in browsers:
        try:
            result = getattr(browser, "stop")()
            if inspect.isawaitable(result):
                run_async(result, timeout=10)  # type: ignore[arg-type]
        except Exception:
            logger.exception("Failed to stop browser during cleanup")
        finally:
            release_browser(browser)


atexit.register(cleanup_drivers)
