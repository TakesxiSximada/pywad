#-*- coding: utf-8 -*-
"""The part runner.
"""
from .error import BrowserClose, BrowserNoClose
from .part import Jump
from .browser.firefox import FirefoxFactory
import time


class Runner(list):
    """The part runner object.
    """

    def __init__(self, browser=None, status=dict, interval=1, sleep=1):
        """Constructor.
        """
        self._browser_or_factory = browser
        self._status_or_factory = status
        self._interval = int(interval)
        self._sleep = int(sleep)

    def interval(self):
        """Sleep by unit cycle.
        """
        time.sleep(self._interval)
        return True

    def sleep(self):
        """Sleep by during running elements.
        """
        time.sleep(self._sleep)
        return True

    def get_browser(self):
        """Create browser.
        """
        browser_or_factory = self._browser_or_factory or FirefoxFactory()
        try:
            return browser_or_factory()
        except TypeError:
            return browser_or_factory

    def get_status(self):
        """Create status object.
        """
        try:
            return self._status_or_factory()
        except TypeError:
            return self._status_or_factory

    def run(self, url=None):
        """Run elements.
        """
        browser = self.get_browser()
        status = self.get_status()
        if url:
            jump = Jump(url)
            jump.start(browser, status)
        try:
            while self.interval():
                for part in self:
                    part.start(browser, status)
                    self.sleep()
        except BrowserClose:
            browser.close()
        except BrowserNoClose:
            pass
