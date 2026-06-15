import os
from typing import cast
import unittest
from unittest.mock import patch

from lncrawl.webdriver.job_queue import (
    BROWSER_USE_SESSION_TTL_SECONDS,
    BrowserPoolKey,
    acquire_browser,
    cleanup_drivers,
    release_browser,
)


class FakeBrowser:
    def __init__(self, name):
        self.name = name
        self.stop_count = 0

    def stop(self):
        self.stop_count += 1


class TestBrowserPool(unittest.TestCase):
    def setUp(self):
        cleanup_drivers()

    def tearDown(self):
        cleanup_drivers()

    @patch.dict(os.environ, {"BROWSER_USE_CONCURRENCY": "1"})
    def test_reuse_before_ttl(self):
        key = BrowserPoolKey(api_key="", user_data_dir="/tmp/test", headless=True, extra_args=())
        created = []

        def factory():
            browser = FakeBrowser(f"browser-{len(created)}")
            created.append(browser)
            return browser

        b1 = cast(FakeBrowser, acquire_browser(key, factory))
        self.assertEqual(len(created), 1)
        self.assertEqual(created[0].stop_count, 0)

        release_browser(b1, reusable=True)
        b2 = cast(FakeBrowser, acquire_browser(key, factory))
        self.assertIs(b1, b2)
        self.assertEqual(len(created), 1)
        self.assertEqual(created[0].stop_count, 0)

        release_browser(b2, reusable=True)

    @patch.dict(os.environ, {"BROWSER_USE_CONCURRENCY": "1"})
    @patch("lncrawl.webdriver.job_queue.time.monotonic")
    def test_replace_after_ttl(self, mock_monotonic):
        base_time = 1000.0
        mock_monotonic.return_value = base_time

        key = BrowserPoolKey(api_key="", user_data_dir="/tmp/test", headless=True, extra_args=())
        created = []

        def factory():
            browser = FakeBrowser(f"browser-{len(created)}")
            created.append(browser)
            return browser

        b1 = cast(FakeBrowser, acquire_browser(key, factory))
        release_browser(b1, reusable=True)

        mock_monotonic.return_value = base_time + BROWSER_USE_SESSION_TTL_SECONDS + 1

        b2 = cast(FakeBrowser, acquire_browser(key, factory))
        self.assertIsNot(b1, b2)
        self.assertEqual(len(created), 2)
        self.assertEqual(b1.stop_count, 1)

        release_browser(b2, reusable=True)


if __name__ == "__main__":
    unittest.main()
