#-*- coding: utf-8 -*-
"""The browser controller.
"""
from .decorator import browser_control


class Part(object):
    """The browser controller object.
    """

    hook_setup_parts = []
    hook_run_parts = []
    hook_teardown_parts = []
    hook_force_parts = []

    def start(self, browser, status):
        """Start controlling browser.
        """
        print self.__class__.__name__, '--->',
        if self.is_target(browser, status):
            print 'GO'
            self.setup(browser, status)
            self.run(browser, status)
            self.teardown(browser, status)
            return True
        else:
            print 'PASS'
            return False

    def is_target(self, browser, status):
        """Check whether or not to perform.
        """
        return True

    @browser_control
    def force(self, browser, status):
        """Force execute first.
        """
        return self.hook_force_parts

    @browser_control
    def setup(self, browser, sttus):
        """Execute first.
        """
        return self.hook_setup_parts

    @browser_control
    def teardown(self, browser, status):
        """Execute last.
        """
        return self.hook_teardown_parts

    @browser_control
    def run(self, browser, status):
        """Execute controlling browser main.
        """
        return self.hook_run_parts


class Jump(Part):
    """Simple URL jump Part.
    """
    default_url = 'http://www.google.com'

    def __init__(self, url=None):
        """Constructor.
        """
        self.url = url or self.default_url

    def run(self, browser, status):
        """Jump the URL.
        """
        browser.get(self.url)
