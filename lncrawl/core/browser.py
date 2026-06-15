import asyncio
import base64
from enum import Enum
import json
import logging
from typing import TYPE_CHECKING, Any, List, Optional

from requests.cookies import RequestsCookieJar
from scraper import PageSoup

from ..context import ctx
from ..utils.async_loop import run_async
from ..webdriver import create_new
from ..webdriver.storage import BrowserStorage

if TYPE_CHECKING:
    from browser_use.actor.element import Element
    from browser_use.actor.page import Page
    from browser_use.browser.session import BrowserSession

logger = logging.getLogger(__name__)

# ----------------------------------------------------------------------------- #
# Selector helpers
# ----------------------------------------------------------------------------- #

_xpath_seq = 0


class By(str, Enum):
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"

    def __str__(self) -> str:
        return self.value


def _to_css(selector: str, by: By) -> str:
    if by == By.CSS_SELECTOR:
        return selector
    elif by == By.ID:
        return f"#{selector}"
    elif by == By.CLASS_NAME:
        return f".{selector}"
    elif by == By.TAG_NAME:
        return selector
    elif by == By.NAME:
        return f"[name='{selector}']"
    else:
        raise ValueError(f"Cannot convert {by} to CSS selector")


def _xpath_literal(value: str) -> str:
    if "'" not in value:
        return f"'{value}'"
    if '"' not in value:
        return f'"{value}"'
    parts = value.split("'")
    return "concat(" + ', "\'", '.join(f"'{part}'" for part in parts) + ")"


def _link_text_xpath(selector: str, partial: bool, relative: bool = False) -> str:
    root = ".//a" if relative else "//a"
    literal = _xpath_literal(selector)
    if partial:
        return f"{root}[contains(normalize-space(.), {literal})]"
    return f"{root}[normalize-space(.) = {literal}]"


def _selector_xpath(selector: str, by: By, relative: bool = False) -> Optional[str]:
    if by == By.XPATH:
        return selector
    if by == By.LINK_TEXT:
        return _link_text_xpath(selector, partial=False, relative=relative)
    if by == By.PARTIAL_LINK_TEXT:
        return _link_text_xpath(selector, partial=True, relative=relative)
    return None


def _make_xpath_attr(prefix: str = "xpath") -> str:
    global _xpath_seq
    _xpath_seq += 1
    return f"data-lncrawl-{prefix}-{_xpath_seq}"


async def _cleanup_marked(elements: List["Element"], attr: str) -> None:
    script = f"() => this.removeAttribute({json.dumps(attr)})"
    for elem in elements:
        try:
            await elem.evaluate(script)
        except Exception:
            pass


async def _page_xpath_all(page: "Page", xpath: str) -> List["Element"]:
    attr = _make_xpath_attr()
    await page.evaluate(
        f"""() => {{
            const result = document.evaluate(
                {json.dumps(xpath)},
                document,
                null,
                XPathResult.ORDERED_NODE_ITERATOR_TYPE,
                null
            );
            let node;
            while ((node = result.iterateNext())) {{
                if (node && node.setAttribute) {{
                    node.setAttribute({json.dumps(attr)}, "");
                }}
            }}
            return true;
        }}"""
    )
    elements = await page.get_elements_by_css_selector(f"[{attr}]")
    await _cleanup_marked(elements, attr)
    return elements


async def _element_xpath_all(page: "Page", elem: "Element", xpath: str) -> List["Element"]:
    attr = _make_xpath_attr()
    await elem.evaluate(
        f"""() => {{
            const result = document.evaluate(
                {json.dumps(xpath)},
                this,
                null,
                XPathResult.ORDERED_NODE_ITERATOR_TYPE,
                null
            );
            let node;
            while ((node = result.iterateNext())) {{
                if (node && node.setAttribute) {{
                    node.setAttribute({json.dumps(attr)}, "");
                }}
            }}
            return true;
        }}"""
    )
    elements = await page.get_elements_by_css_selector(f"[{attr}]")
    await _cleanup_marked(elements, attr)
    return elements


async def _element_css_all(page: "Page", elem: "Element", css: str) -> List["Element"]:
    attr = _make_xpath_attr("css")
    await elem.evaluate(
        f"""() => {{
            const nodes = this.querySelectorAll({json.dumps(css)});
            for (const node of nodes) {{
                node.setAttribute({json.dumps(attr)}, "");
            }}
            return true;
        }}"""
    )
    elements = await page.get_elements_by_css_selector(f"[{attr}]")
    await _cleanup_marked(elements, attr)
    return elements


async def _page_find_all(page: "Page", selector: str, by: By) -> List["Element"]:
    try:
        xpath = _selector_xpath(selector, by)
        if xpath:
            return await _page_xpath_all(page, xpath)
        return await page.get_elements_by_css_selector(_to_css(selector, by))
    except Exception:
        return []


async def _page_find(page: "Page", selector: str, by: By) -> Optional["Element"]:
    elements = await _page_find_all(page, selector, by)
    return elements[0] if elements else None


async def _element_find_all(
    page: "Page",
    elem: "Element",
    selector: str,
    by: By,
) -> List["Element"]:
    try:
        xpath = _selector_xpath(selector, by, relative=True)
        if xpath:
            return await _element_xpath_all(page, elem, xpath)
        return await _element_css_all(page, elem, _to_css(selector, by))
    except Exception:
        return []


async def _element_find(
    page: "Page",
    elem: "Element",
    selector: str,
    by: By,
) -> Optional["Element"]:
    elements = await _element_find_all(page, elem, selector, by)
    return elements[0] if elements else None


def _wrap_js(script: str, is_async: bool = False) -> str:
    prepared = script.strip()
    if prepared.endswith(";"):
        prepared = prepared[:-1].rstrip()
    if "=>" in prepared:
        if prepared.startswith("("):
            if prepared.endswith(")()"):
                return prepared[:-2].rstrip()
            return prepared
        if prepared.startswith("async"):
            return f"({prepared})"
    if is_async:
        return f"(async () => {{ {script} }})"
    return f"() => {{ {script} }}"


def _normalize_js_result(value: Any) -> Any:
    if not isinstance(value, str):
        return value

    text = value.strip()
    if not text:
        return value
    if text in ("True", "true"):
        return True
    if text in ("False", "false"):
        return False
    if text in ("None", "null"):
        return None
    if text[0] in "[{":
        try:
            return json.loads(text)
        except Exception:
            return value
    try:
        if text.isdigit() or (text[0] == "-" and text[1:].isdigit()):
            return int(text)
    except IndexError:
        pass
    return value


# ----------------------------------------------------------------------------- #
# WebElement
# ----------------------------------------------------------------------------- #


class WebElement:
    def __init__(self, page: "Page", elem: "Element") -> None:
        self._page = page
        self._elem = elem

    @property
    def text(self) -> str:
        return run_async(self._elem.evaluate("() => this.textContent || ''")) or ""

    @property
    def tag_name(self) -> str:
        return run_async(self._elem.evaluate("() => (this.tagName || '').toLowerCase()")) or ""

    def get_attribute(self, name: str) -> Optional[str]:
        value = run_async(self._elem.get_attribute(name))
        if value is not None:
            return value

        js_name = json.dumps(name)
        missing = "__LNC_ATTR_MISSING__"
        fallback = run_async(
            self._elem.evaluate(
                f"() => {{ const name = {js_name}; if (!(name in this)) return {json.dumps(missing)}; const value = this[name]; return value == null ? {json.dumps(missing)} : String(value); }}"
            )
        )
        return None if fallback == missing else fallback

    @property
    def outer_html(self) -> str:
        return run_async(self._elem.evaluate("() => this.outerHTML || ''")) or ""

    def as_tag(self) -> PageSoup:
        html = self.outer_html
        if not hasattr(self, "_cached_html") or self._cached_html != html:
            self._cached_html = html
            self._cached_tag = PageSoup.create(html)
        return self._cached_tag  # type: ignore[return-value]

    def find_all(self, selector: str, by: By = By.CSS_SELECTOR) -> List["WebElement"]:
        elements = run_async(_element_find_all(self._page, self._elem, selector, by)) or []
        return [WebElement(self._page, e) for e in elements]

    def find(self, selector: str, by: By = By.CSS_SELECTOR) -> Optional["WebElement"]:
        elem = run_async(_element_find(self._page, self._elem, selector, by))
        return WebElement(self._page, elem) if elem else None

    def click(self) -> None:
        run_async(self._elem.click())

    def send_keys(self, text: str) -> None:
        run_async(self._elem.fill(text, clear=False))

    def clear(self) -> None:
        run_async(self._elem.fill("", clear=True))

    def submit(self) -> None:
        run_async(
            self._elem.evaluate(
                "() => { const form = this.form || this.closest('form'); if (form) form.submit(); }"
            )
        )

    def remove(self) -> None:
        run_async(self._elem.evaluate("() => this.remove()"))

    def scroll_into_view(self) -> None:
        run_async(
            self._elem.evaluate(
                "() => this.scrollIntoViewIfNeeded ? this.scrollIntoViewIfNeeded() : this.scrollIntoView({block: 'center', inline: 'center'})"
            )
        )

    @property
    def screenshot_as_png(self) -> bytes:
        data = run_async(self._elem.screenshot(format="png"))
        return base64.b64decode(data)


# ----------------------------------------------------------------------------- #
# Browser
# ----------------------------------------------------------------------------- #


class Browser:
    def __init__(
        self,
        headless: bool = False,
        timeout: Optional[int] = 120,
        extra_args: Optional[List[str]] = None,
        cookie_store: Optional[RequestsCookieJar] = None,
    ) -> None:
        self.extra_args = extra_args
        self.timeout = timeout
        self.headless = headless
        self.cookie_store = cookie_store
        self._page: Optional["Page"] = None
        self._browser: Optional["BrowserSession"] = None
        self.local_storage = BrowserStorage(self, "localStorage")
        self.session_storage = BrowserStorage(self, "sessionStorage")

    def __del__(self) -> None:
        self.close()

    def __enter__(self) -> "Browser":
        self.open_browser()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close(reusable=exc_type is None)

    def close(self, reusable: bool = True) -> None:
        if not self._browser:
            return

        from ..webdriver.job_queue import release_browser

        browser = self._browser
        ctx.logger.debug("Closing browser")
        release_browser(browser, reusable=reusable, timeout=self.timeout)
        self._browser = None
        self._page = None
        self._html_ = None
        self._soup_ = None

    def open_browser(self) -> None:
        if self._browser:
            return
        ctx.logger.debug("Opening browser")

        self._browser = create_new(
            extra_args=self.extra_args,
            timeout=self.timeout,
            headless=self.headless,
        )
        self._page = run_async(self._browser.get_current_page(), timeout=self.timeout)
        if not self._page:
            self._page = run_async(self._browser.new_page("about:blank"), timeout=self.timeout)

    @property
    def active(self) -> bool:
        from ..webdriver.job_queue import check_active

        return check_active(self._browser)

    @property
    def current_url(self) -> Optional[str]:
        try:
            if self._page:
                return run_async(self._page.get_url(), timeout=self.timeout) or None
            if self._browser:
                return run_async(self._browser.get_current_page_url(), timeout=self.timeout) or None
        except Exception:
            return None
        return None

    @property
    def session_id(self) -> Optional[str]:
        if not self._page:
            return None
        return getattr(self._page, "_target_id", None)

    @property
    def html(self) -> str:
        if not self._page:
            return ""
        try:
            return (
                run_async(
                    self._page.evaluate("() => document.documentElement.outerHTML || ''"),
                    timeout=self.timeout,
                )
                or ""
            )
        except Exception:
            return ""

    @property
    def soup(self) -> PageSoup:
        old_html = getattr(self, "_html_", None)
        current = self.html
        if old_html == current:
            return getattr(self, "_soup_")  # type: ignore[return-value]
        soup = PageSoup.create(current)
        setattr(self, "_html_", current)
        setattr(self, "_soup_", soup)
        return soup

    def visit(self, url: str) -> None:
        self.open_browser()
        if self._browser:
            run_async(self._browser.navigate_to(url), timeout=self.timeout)
            self._page = run_async(self._browser.get_current_page(), timeout=self.timeout)

    def find_all(self, selector: str, by: By = By.CSS_SELECTOR) -> List[WebElement]:
        if not self._page:
            return []
        elements = run_async(_page_find_all(self._page, selector, by), timeout=self.timeout)
        return [WebElement(self._page, e) for e in elements]

    def find(self, selector: str, by: By = By.CSS_SELECTOR) -> Optional[WebElement]:
        if not self._page:
            return None
        elem = run_async(_page_find(self._page, selector, by), timeout=self.timeout)
        return WebElement(self._page, elem) if elem else None

    def click(self, selector: str, by: By = By.CSS_SELECTOR) -> None:
        elem = self.find(selector, by)
        if elem:
            elem.scroll_into_view()
            elem.click()

    def submit(self, selector: str, by: By = By.CSS_SELECTOR) -> None:
        elem = self.find(selector, by)
        if elem:
            elem.scroll_into_view()
            elem.submit()

    def send_keys(
        self,
        selector: str,
        by: By = By.CSS_SELECTOR,
        text: str = "",
        clear: bool = True,
    ) -> None:
        elem = self.find(selector, by)
        if elem:
            elem.scroll_into_view()
            if clear:
                elem.clear()
            elem.send_keys(text)

    def execute_js(self, script: str, is_async: bool = False) -> Any:
        """Execute JavaScript in the current page. Use is_async for async scripts."""
        if not self._page:
            return None
        try:
            result = run_async(
                self._page.evaluate(_wrap_js(script, is_async=is_async)),
                timeout=self.timeout,
            )
            return _normalize_js_result(result)
        except Exception as e:
            ctx.logger.debug("execute_js error | %s", e)
            return None

    def wait(
        self,
        selector: str,
        by: By = By.CSS_SELECTOR,
        timeout: Optional[float] = None,
        poll_frequency: Optional[float] = 0.25,
        inverse: bool = False,
    ) -> None:
        """Wait until an element matching selector appears (or disappears if inverse=True)."""
        if not self._page or not selector:
            return
        wait_secs = float(timeout or 60)
        poll = float(poll_frequency or 0.25)
        ctx.logger.debug("Wait %.1fs for %s:%s (inverse=%s)", wait_secs, by, selector, inverse)

        try:
            completed = run_async(
                self._wait_for(selector, by, wait_secs, bool(inverse), poll),
                timeout=wait_secs + 5,
            )
            if not completed:
                ctx.logger.info("wait() timed out for %s:%s", by, selector)
        except Exception as e:
            ctx.logger.info("wait() did not finish cleanly | %s", e)

    async def _wait_for(
        self,
        selector: str,
        by: By,
        timeout: float,
        inverse: bool,
        poll: float,
    ) -> bool:
        assert self._page is not None
        deadline = asyncio.get_event_loop().time() + timeout
        while asyncio.get_event_loop().time() < deadline:
            elem = await _page_find(self._page, selector, by)
            if (not inverse and elem) or (inverse and not elem):
                return True
            await asyncio.sleep(poll)
        return False
