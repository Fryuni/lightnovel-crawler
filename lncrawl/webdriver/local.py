import logging
import os
from typing import List, NamedTuple, Optional

from ..exceptions import LNException
from ..utils.browser_detect import pick_executable
from ..utils.platforms import Platform, Screen

logger = logging.getLogger(__name__)


class LocalBrowserOptions(NamedTuple):
    executable: str
    headless: bool
    browser_args: List[str]
    sandbox: bool
    width: int
    height: int


def get_local_browser_options(
    extra_args: Optional[List[str]] = None,
    headless: bool = False,
) -> LocalBrowserOptions:
    """Build BrowserUse local-browser launch options."""
    executable = pick_executable()
    if not executable:
        raise LNException(
            "No Chromium-based browser found. "
            "Please install Chrome, Edge, Brave, Vivaldi, Yandex, or Whale."
        )

    if not headless and not Platform.has_display:
        headless = True

    if headless:
        width = int(os.getenv("CHROME_WIDTH", "1920"))
        height = int(os.getenv("CHROME_HEIGHT", "1080"))
    else:
        width = max(640, Screen.view_width * 3 // 4)
        height = max(480, Screen.view_height * 3 // 4)
        width = int(os.getenv("CHROME_WIDTH", width))
        height = int(os.getenv("CHROME_HEIGHT", height))

    browser_args = [f"--window-size={width},{height}"]
    if extra_args:
        browser_args += extra_args

    is_debug = bool(os.getenv("debug_mode"))
    if not is_debug:
        browser_args += ["--log-level=3", "--disable-logging"]

    # Disable sandbox when headless on Linux/Docker/CI — Chrome requires this
    # when running as root or in restricted container environments.
    sandbox = not (headless and (Platform.linux or Platform.docker or Platform.ci))

    return LocalBrowserOptions(
        executable=executable,
        headless=headless,
        browser_args=browser_args,
        sandbox=sandbox,
        width=width,
        height=height,
    )
