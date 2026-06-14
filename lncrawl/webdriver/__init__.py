import logging
import os
from typing import List, Optional

from ..context import ctx
from ..utils.async_loop import run_async
from .job_queue import _release_queue_slot, acquire_queue, register_browser

logger = logging.getLogger(__name__)


def create_new(
    extra_args: Optional[List[str]] = None,
    timeout: Optional[float] = None,
    user_data_dir: Optional[str] = None,
    headless: bool = False,
    **kwargs,
):
    """Create and start a BrowserUse browser session."""
    os.environ.setdefault("BROWSER_USE_SETUP_LOGGING", "false")

    from browser_use import Browser

    api_key = (
        ctx.config.crawler.browser_use_api_key or os.getenv("BROWSER_USE_API_KEY", "")
    ).strip()

    acquire_queue(timeout)
    try:
        if api_key:
            os.environ["BROWSER_USE_API_KEY"] = api_key
            browser = Browser(use_cloud=True)
            mode = "remote"
        else:
            if not user_data_dir:
                user_data_dir = str(ctx.config.app.app_dir / "webdriver")
                os.makedirs(user_data_dir, exist_ok=True)

            from .local import get_local_browser_options

            options = get_local_browser_options(
                extra_args=extra_args,
                headless=headless,
            )
            browser = Browser(
                headless=options.headless,
                executable_path=options.executable,
                user_data_dir=user_data_dir,
                args=options.browser_args,
                chromium_sandbox=options.sandbox,
                window_size={"width": options.width, "height": options.height},
            )
            mode = "local"

        run_async(browser.start(), timeout=timeout)
        register_browser(browser)
        logger.info("Created BrowserUse browser instance (mode=%s)", mode)
        return browser
    except Exception:
        _release_queue_slot()
        raise
