from __future__ import annotations

import logging
import os
from typing import TYPE_CHECKING, List, Optional

from ..context import ctx
from ..utils.async_loop import run_async
from .job_queue import BrowserPoolKey, acquire_browser

if TYPE_CHECKING:
    from browser_use import Browser

logger = logging.getLogger(__name__)


def create_new(
    extra_args: Optional[List[str]] = None,
    timeout: Optional[float] = None,
    user_data_dir: Optional[str] = None,
    headless: bool = False,
    **kwargs,
) -> Browser:
    """Create and start a BrowserUse browser session."""
    os.environ.setdefault("BROWSER_USE_SETUP_LOGGING", "false")

    from browser_use import Browser as BrowserUseBrowser

    api_key = (
        ctx.config.crawler.browser_use_api_key or os.getenv("BROWSER_USE_API_KEY", "")
    ).strip()

    if api_key:
        key = BrowserPoolKey(
            api_key=api_key,
            user_data_dir="",
            headless=headless,
            extra_args=tuple(extra_args or ()),
        )

        def factory() -> BrowserUseBrowser:
            os.environ["BROWSER_USE_API_KEY"] = api_key
            browser = BrowserUseBrowser(use_cloud=True)
            run_async(browser.start(), timeout=timeout)
            logger.info("Created BrowserUse browser instance (mode=%s)", "remote")
            return browser
    else:
        if not user_data_dir:
            user_data_dir = str(ctx.config.app.app_dir / "webdriver")
            os.makedirs(user_data_dir, exist_ok=True)

        from .local import get_local_browser_options

        options = get_local_browser_options(
            extra_args=extra_args,
            headless=headless,
        )
        key = BrowserPoolKey(
            api_key="",
            user_data_dir=user_data_dir,
            headless=options.headless,
            extra_args=tuple(options.browser_args),
        )

        def factory() -> BrowserUseBrowser:
            browser = BrowserUseBrowser(
                headless=options.headless,
                executable_path=options.executable,
                user_data_dir=user_data_dir,
                args=options.browser_args,
                chromium_sandbox=options.sandbox,
                window_size={"width": options.width, "height": options.height},
            )
            run_async(browser.start(), timeout=timeout)
            logger.info("Created BrowserUse browser instance (mode=%s)", "local")
            return browser

    return acquire_browser(key, factory, api_key=api_key)  # type: ignore[return-value]
