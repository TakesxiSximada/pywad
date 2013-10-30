#-*- coding: utf-8 -*-
"""The exceptions.
"""


class BrowserFinish(Exception):
    """The browser finish instruction.
    """
    pass


class BrowserClose(BrowserFinish):
    """The browser close instruction.
    """
    pass


class BrowserNoClose(BrowserFinish):
    """The browser no close instruction.
    """
    pass
