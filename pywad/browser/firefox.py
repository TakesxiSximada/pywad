#-*- coding: utf-8 -*-
from selenium.webdriver import Firefox, Proxy, FirefoxProfile


class FirefoxFactory(object):
    """The borwser factory class of Firefox.
    """

    default_profile = {
        'security.warn_entering_secure': False,
        'security.warn_entering_secure.show_once': True,
        'security.warn_entering_weak': False,
        'security.warn_entering_weak._show_once': True,
        'security.warn_leaving_secure': False,
        'security.warn_leaving_secure.show_once': True,
        'security.warn_leaving_weak': False,
        'security.warn_leaving_weak._show_once': True,
        'security.warn_submit_insecure': False,
        'security.warn_viewing_mixed': False,
        'security.warn_viewing_mixed.show_once': True,
        }

    def __init__(self, proxy=None, implicitly_wait=10, clear_cookies=False):
        """Constructor.
        """
        self.implicitly_wait = implicitly_wait
        self.clear_cookies = clear_cookies
        self.proxy = proxy

    def _create_proxy_setting(self):
        """Create proxy object.
        """
        proxy = Proxy()
        if self.proxy:
            proxy.ftp_proxy = proxy.ssl_proxy = proxy.http_proxy = self.proxy
        return proxy

    def _create_profile(self):
        """Create profile object.
        """
        profile = FirefoxProfile()
        for name, value in self.default_profile.items():
            profile.set_preference(name, value)
        return profile

    def _create_browser_instance(self):
        """Start browser.
        """
        profile = self._create_profile()
        proxy = self._create_proxy_setting()
        return Firefox(firefox_profile=profile, proxy=proxy)

    def create(self):
        """The browser factory method.
        """
        browser = self._create_browser_instance()
        browser.implicitly_wait(self.implicitly_wait)
        if self.clear_cookies:
            browser.delete_allcookies()
        return browser

    def __call__(self):
        """Emurate factory function.
        """
        return self.create()
