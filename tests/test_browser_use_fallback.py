import unittest
from unittest.mock import patch

import requests
from requests.cookies import RequestsCookieJar
from requests.utils import CaseInsensitiveDict
from scraper import PageSoup

from lncrawl.core.browser_scraper import BrowserUseScraper


class FakeScraper:
    def __init__(self):
        self.origin = "https://example.com"
        self.headers = CaseInsensitiveDict()
        self.cookies = RequestsCookieJar()
        self.signal = None
        self._responses: dict = {}
        self._calls = []
        self._error: Exception = RuntimeError("not configured")

    def get_soup(self, url, **kwargs):
        self._calls.append(("get_soup", url, kwargs))
        if "get_soup" in self._responses:
            return self._responses["get_soup"]
        raise self._error

    def get(self, url, **kwargs):
        self._calls.append(("get", url, kwargs))
        if "get" in self._responses:
            return self._responses["get"]
        raise self._error

    def get_json(self, url, **kwargs):
        self._calls.append(("get_json", url, kwargs))
        if "get_json" in self._responses:
            return self._responses["get_json"]
        raise self._error

    def post(self, url, **kwargs):
        self._calls.append(("post", url, kwargs))
        if "post" in self._responses:
            return self._responses["post"]
        raise self._error

    def close(self):
        self._calls.append(("close", None, {}))

    def set_success(self, method, value):
        self._responses[method] = value

    def set_error(self, exc):
        self._error = exc
        self._responses = {}


class FakeBrowser:
    def __init__(self, soup=None, current_url=""):
        self._soup = soup
        self._current_url = current_url
        self._visits = []
        self._waits = []
        self._scripts = []
        self._closed = False
        self._close_reusable = None

    def visit(self, url):
        self._visits.append(url)

    def wait(self, selector, by, timeout=60):
        self._waits.append((selector, by, timeout))

    @property
    def current_url(self):
        return self._current_url

    @property
    def soup(self):
        return self._soup

    @property
    def html(self):
        return str(self._soup) if self._soup else ""

    def execute_js(self, script, is_async=False):
        self._scripts.append((script, is_async))
        return ""

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close(reusable=exc_type is None)

    def close(self, reusable=True):
        self._closed = True
        self._close_reusable = reusable


class TestBrowserUseScraperDirectFirst(unittest.TestCase):
    def setUp(self):
        self.fake_scraper = FakeScraper()
        self.adapter = BrowserUseScraper(self.fake_scraper)  # type: ignore[arg-type]

    @patch("lncrawl.core.browser_scraper.Browser")
    def test_get_soup_direct_success_no_browser(self, mock_browser_cls):
        mock_browser_cls.side_effect = AssertionError("Browser should not be constructed")
        direct_soup = PageSoup.create("<html><body><p>direct</p></body></html>")
        self.fake_scraper.set_success("get_soup", direct_soup)

        result = self.adapter.get_soup("https://example.com/page")

        self.assertIn("direct", result.find("p").text)
        self.assertEqual(len(self.fake_scraper._calls), 1)
        self.assertEqual(self.fake_scraper._calls[0][0], "get_soup")
        mock_browser_cls.assert_not_called()

    @patch("lncrawl.core.browser_scraper.Browser")
    def test_get_soup_fallback_on_direct_failure(self, mock_browser_cls):
        fake_browser = FakeBrowser(
            soup=PageSoup.create("<html><body><p>browser</p></body></html>"),
            current_url="https://example.com/page",
        )
        mock_browser_cls.return_value = fake_browser
        self.fake_scraper.set_error(requests.ConnectionError("blocked"))

        result = self.adapter.get_soup("https://example.com/page")

        self.assertIn("browser", result.find("p").text)
        self.assertEqual(len(self.fake_scraper._calls), 1)
        self.assertEqual(self.fake_scraper._calls[0][0], "get_soup")
        self.assertEqual(fake_browser._visits, ["https://example.com/page"])
        self.assertTrue(fake_browser._closed)

    @patch("lncrawl.core.browser_scraper.Browser")
    def test_get_direct_success_no_browser(self, mock_browser_cls):
        mock_browser_cls.side_effect = AssertionError("Browser should not be constructed")
        response = requests.Response()
        response.status_code = 200
        response._content = b"ok"
        self.fake_scraper.set_success("get", response)

        result = self.adapter.get("https://example.com/page")

        self.assertEqual(result.status_code, 200)
        self.assertEqual(len(self.fake_scraper._calls), 1)
        self.assertEqual(self.fake_scraper._calls[0][0], "get")
        mock_browser_cls.assert_not_called()


if __name__ == "__main__":
    unittest.main()
