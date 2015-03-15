# -*- coding: utf-8 -*-
"""Pywad utilities for selenium.
"""
import zope.dottedname.resolve


def get_driver(name):
    """Get selenium.webdriver.*.webdriver.WebDriver class object from driver name.
    """
    module_name = 'selenium.webdriver.{}.webdriver'.format(name)
    target = '{}.WebDriver'.format(module_name)
    return zope.dottedname.resolve.resolve(target, module_name)
