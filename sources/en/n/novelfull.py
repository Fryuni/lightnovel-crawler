# -*- coding: utf-8 -*-
import logging

from lncrawl.templates.novelfull import NovelFullTemplate

logger = logging.getLogger(__name__)


class NovelFullCrawler(NovelFullTemplate):
    can_search = True
    search_item_list_selector = "#list-page .archive .list-truyen > .row"
    search_item_title_selector = "h3[class*='title'] > a"
    search_item_url_selector = "h3[class*='title'] > a"
    search_item_info_selector = ".chapter-text, span.chapter"
    base_url = [
        "http://novelfull.com/",
        "https://novelfull.com/",
        "https://novelfull.net/",
    ]

    def initialize(self) -> None:
        self.cleaner.bad_css.update(
            [
                'div[align="left"]',
                'img[src*="proxy?container=focus"]',
            ]
        )
