import atexit
import inspect
import logging
from threading import Semaphore
from typing import List, Optional

from ..utils.async_loop import run_async

logger = logging.getLogger(__name__)

MAX_BROWSER_INSTANCES = 8

__open_browsers: List[object] = []
__semaphore = Semaphore(MAX_BROWSER_INSTANCES)


def acquire_queue(timeout: Optional[float] = None) -> None:
    acquired = __semaphore.acquire(True, timeout)
    if not acquired:
        raise TimeoutError("Failed to acquire browser semaphore")


def _find_browser_index(browser: object) -> Optional[int]:
    for index, open_browser in enumerate(__open_browsers):
        if open_browser is browser:
            return index
    return None


def _release_queue_slot() -> None:
    __semaphore.release()


def register_browser(browser: object) -> None:
    if _find_browser_index(browser) is None:
        __open_browsers.append(browser)


def release_browser(browser: object) -> None:
    index = _find_browser_index(browser)
    if index is not None:
        __open_browsers.pop(index)
        __semaphore.release()
        logger.info("Destroyed browser instance")


def check_active(browser: Optional[object]) -> bool:
    return browser is not None and _find_browser_index(browser) is not None


def cleanup_drivers() -> None:
    for browser in list(__open_browsers):
        try:
            result = getattr(browser, "stop")()
            if inspect.isawaitable(result):
                run_async(result, timeout=10)  # type: ignore[arg-type]
        except Exception:
            logger.exception("Failed to stop browser during cleanup")
        finally:
            release_browser(browser)


atexit.register(cleanup_drivers)
