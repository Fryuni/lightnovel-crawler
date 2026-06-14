from __future__ import annotations

from http.cookies import SimpleCookie
import json as jsonlib
import threading
from typing import Any, Mapping, MutableMapping, Optional, Union
from urllib.parse import urlencode, urlsplit, urlunsplit

import requests
from requests.cookies import RequestsCookieJar
from requests.utils import CaseInsensitiveDict
from scraper import PageSoup, Scraper

from ..context import ctx
from ..utils.url_tools import extract_base
from .browser import Browser, By


class BrowserUseResponse(requests.Response):
    def __init__(
        self,
        url: str,
        status_code: int,
        headers: CaseInsensitiveDict,
        text: str,
    ) -> None:
        super().__init__()
        self.url = url
        self.status_code = status_code
        self.headers = headers
        self._content = text.encode()
        self.encoding = "utf-8"

    def json(self, **kwargs: Any) -> Any:
        return jsonlib.loads(self.text, **kwargs)

    def raise_for_status(self) -> None:
        if 200 <= self.status_code < 400:
            return
        message = f"{self.status_code} Error for url: {self.url}"
        raise requests.HTTPError(message, response=self)


class BrowserUseScraper:
    def __init__(self, scraper: Scraper) -> None:
        self._scraper = scraper
        self._browser: Optional[Browser] = None
        self._lock = threading.RLock()

    @property
    def origin(self) -> str:
        return self._scraper.origin

    @origin.setter
    def origin(self, value: str) -> None:
        self._scraper.origin = value

    @property
    def headers(self) -> MutableMapping:
        return self._scraper.headers

    @headers.setter
    def headers(self, value: MutableMapping) -> None:
        self._scraper.headers = value

    @property
    def cookies(self) -> RequestsCookieJar:
        return self._scraper.cookies

    @cookies.setter
    def cookies(self, value: Any) -> None:
        self._scraper.cookies = value

    @property
    def signal(self) -> Any:
        return self._scraper.signal

    @signal.setter
    def signal(self, value: Any) -> None:
        self._scraper.signal = value

    @property
    def last_soup_url(self) -> str:
        return self._scraper.last_soup_url

    @last_soup_url.setter
    def last_soup_url(self, value: str) -> None:
        self._scraper.last_soup_url = value

    def __getattr__(self, name: str) -> Any:
        return getattr(self._scraper, name)

    def close(self) -> None:
        with self._lock:
            browser = self._browser
            self._browser = None
            try:
                if browser:
                    browser.close()
            finally:
                self._scraper.close()

    def make_soup(self, *args: Any, **kwargs: Any) -> PageSoup:
        return self._scraper.make_soup(*args, **kwargs)

    def get_image(self, *args: Any, **kwargs: Any) -> Any:
        return self._scraper.get_image(*args, **kwargs)

    def get_file(self, *args: Any, **kwargs: Any) -> Any:
        return self._scraper.get_file(*args, **kwargs)

    def get_soup(
        self,
        url: str,
        headers: MutableMapping = {},
        encoding: Optional[str] = None,
        params: Optional[Union[Mapping, str]] = None,
        **kwargs: Any,
    ) -> PageSoup:
        with self._lock:
            if headers or params:
                response = self.get(url, headers=headers, params=params, **kwargs)
                response.raise_for_status()
                self.last_soup_url = response.url
                self._sync_cookies()
                return PageSoup.create(response.text, encoding=encoding)

            browser = self._get_browser()
            browser.visit(url)
            browser.wait("body", By.TAG_NAME, timeout=kwargs.pop("timeout", 60))
            self.last_soup_url = browser.current_url or url
            self._sync_cookies()
            return browser.soup

    def get_json(
        self,
        url: str,
        headers: MutableMapping = {},
        params: Optional[Union[Mapping, str]] = None,
        **kwargs: Any,
    ) -> Any:
        response = self.get(url, headers=headers, params=params, _expect_json=True, **kwargs)
        response.raise_for_status()
        return jsonlib.loads(response.text)

    def post_json(
        self,
        url: str,
        data: Union[MutableMapping, str, bytes, None] = None,
        json: Union[MutableMapping, str, bytes, None] = None,
        headers: MutableMapping = {},
        params: Optional[Union[Mapping, str]] = None,
        **kwargs: Any,
    ) -> Any:
        response = self.post(url, data=data, json=json, headers=headers, params=params, **kwargs)
        response.raise_for_status()
        return response.json()

    def post_soup(
        self,
        url: str,
        data: Union[MutableMapping, str, bytes, None] = None,
        headers: MutableMapping = {},
        encoding: Optional[str] = None,
        params: Optional[Union[Mapping, str]] = None,
        **kwargs: Any,
    ) -> PageSoup:
        response = self.post(url, data=data, headers=headers, params=params, **kwargs)
        response.raise_for_status()
        return PageSoup.create(response.text, encoding=encoding)

    def submit_form(
        self,
        url: str,
        data: Union[MutableMapping, str, bytes, None] = None,
        json: Union[MutableMapping, str, bytes, None] = None,
        headers: MutableMapping = {},
        multipart: bool = False,
        params: Optional[Union[Mapping, str]] = None,
        **kwargs: Any,
    ) -> BrowserUseResponse:
        response = self.post(
            url,
            data=data,
            json=json,
            headers=headers,
            params=params,
            multipart=multipart,
            **kwargs,
        )
        response.raise_for_status()
        return response

    def get(
        self,
        url: str,
        headers: MutableMapping = {},
        params: Optional[Union[Mapping, str]] = None,
        **kwargs: Any,
    ) -> BrowserUseResponse:
        expect_json = bool(kwargs.pop("_expect_json", False))
        url = self._with_params(url, params)
        fetch_headers = self._request_headers(headers)
        use_fetch = expect_json or bool(headers) or bool(kwargs)
        with self._lock:
            if use_fetch:
                return self._fetch("GET", url, headers=fetch_headers)

            browser = self._get_browser()
            browser.visit(url)
            browser.wait("body", By.TAG_NAME, timeout=60)
            current_url = browser.current_url or url
            self.last_soup_url = current_url
            self._sync_cookies()
            return BrowserUseResponse(
                url=current_url,
                status_code=200,
                headers=CaseInsensitiveDict(),
                text=browser.html,
            )

    def post(
        self,
        url: str,
        data: Union[MutableMapping, str, bytes, None] = None,
        json: Union[MutableMapping, str, bytes, None] = None,
        headers: MutableMapping = {},
        params: Optional[Union[Mapping, str]] = None,
        **kwargs: Any,
    ) -> BrowserUseResponse:
        multipart = bool(kwargs.pop("multipart", False))
        url = self._with_params(url, params)
        fetch_headers = self._request_headers(headers)
        body = self._request_body(data=data, json=json, headers=fetch_headers, multipart=multipart)
        with self._lock:
            return self._fetch("POST", url, headers=fetch_headers, body=body)

    def _get_browser(self) -> Browser:
        if not self._browser:
            self._browser = Browser(headless=ctx.config.crawler.use_headless_mode)
        return self._browser

    def _fetch(
        self,
        method: str,
        url: str,
        headers: Optional[MutableMapping] = None,
        body: Optional[str] = None,
    ) -> BrowserUseResponse:
        browser = self._get_browser()
        self._visit_fetch_base(browser, url)

        script = f"""
            async () => {{
                const response = await fetch({jsonlib.dumps(url)}, {{
                    method: {jsonlib.dumps(method)},
                    credentials: "include",
                    headers: {jsonlib.dumps(dict(headers or {}))},
                    body: {jsonlib.dumps(body)},
                }});
                return {{
                    url: response.url,
                    status: response.status,
                    ok: response.ok,
                    headers: Array.from(response.headers.entries()),
                    text: await response.text(),
                }};
            }}
        """
        data = browser.execute_js(script, is_async=True)
        if isinstance(data, str):
            data = jsonlib.loads(data)
        if not isinstance(data, dict):
            raise requests.HTTPError(
                f"Browser fetch failed for url: {url}", response=requests.Response()
            )

        response = BrowserUseResponse(
            url=str(data.get("url") or url),
            status_code=int(data.get("status") or 0),
            headers=CaseInsensitiveDict(dict(data.get("headers") or [])),
            text=str(data.get("text") or ""),
        )
        self.last_soup_url = response.url
        self._sync_cookies()
        return response

    def _visit_fetch_base(self, browser: Browser, url: str) -> None:
        parts = urlsplit(url)
        if parts.scheme in ("http", "https") and parts.netloc:
            browser.visit(extract_base(url))
            browser.wait("body", By.TAG_NAME, timeout=60)
        elif not browser.current_url:
            browser.visit("about:blank")

    def _sync_cookies(self) -> None:
        browser = self._browser
        if not browser:
            return
        cookie_header = browser.execute_js("() => document.cookie || ''")
        if not cookie_header:
            return
        cookie = SimpleCookie()
        cookie.load(str(cookie_header))
        for key, morsel in cookie.items():
            self.cookies.set(key, morsel.value)

    def _request_headers(self, headers: Optional[MutableMapping]) -> CaseInsensitiveDict:
        request_headers = CaseInsensitiveDict(self.headers or {})
        request_headers.update(headers or {})
        return request_headers

    def _request_body(
        self,
        data: Union[MutableMapping, str, bytes, None],
        json: Union[MutableMapping, str, bytes, None],
        headers: CaseInsensitiveDict,
        multipart: bool = False,
    ) -> Optional[str]:
        if json is not None:
            if "content-type" not in headers:
                headers["content-type"] = "application/json"
            if isinstance(json, (str, bytes)):
                return json.decode() if isinstance(json, bytes) else json
            return jsonlib.dumps(json)

        if data is None:
            return None
        if isinstance(data, bytes):
            return data.decode()
        if isinstance(data, str):
            return data
        if "content-type" not in headers and not multipart:
            headers["content-type"] = "application/x-www-form-urlencoded;charset=UTF-8"
        return urlencode(data, doseq=True)

    def _with_params(self, url: str, params: Optional[Union[Mapping, str]]) -> str:
        if not params:
            return url
        query = params if isinstance(params, str) else urlencode(params, doseq=True)
        parts = urlsplit(url)
        new_query = "&".join(part for part in (parts.query, query) if part)
        return urlunsplit((parts.scheme, parts.netloc, parts.path, new_query, parts.fragment))
