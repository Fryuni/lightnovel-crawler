import asyncio
from concurrent.futures import Future
import logging
import threading
from typing import Awaitable, Optional, TypeVar

logger = logging.getLogger(__name__)

T = TypeVar("T")

_loop: asyncio.AbstractEventLoop = asyncio.new_event_loop()


async def _await_result(awaitable: Awaitable[T]) -> T:
    return await awaitable


_thread: threading.Thread = threading.Thread(
    target=_loop.run_forever, daemon=True, name="browser-use-loop"
)
_thread.start()


def run_async(coro: Awaitable[T], timeout: Optional[float] = None) -> T:
    """Submit an async awaitable to the browser automation event loop and block until done."""
    future: Future[T] = asyncio.run_coroutine_threadsafe(_await_result(coro), _loop)
    return future.result(timeout=timeout)
