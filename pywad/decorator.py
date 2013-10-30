#-*- coding: utf-8 -*-
"""The decorators.
"""
import re


def browser_control(func):
    """Execute all parts.
    """
    def _wrap(self, browser, status):
        parts = func(self, browser, status)
        for part in parts:
            part.start(browser, status)
    return _wrap


def url_match(pattern):
    """Execute if match to pattern.
    """
    regx = re.compile(pattern)

    def _deco(func):
        def _wrap(self, browser, status):
            url = browser.current_url
            if regx.search(url):
                return func(self, browser, status)
            else:
                return False
        return _wrap
    return _deco
