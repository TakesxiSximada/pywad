#-*- coding: utf-8 -*-
"""The environment etc.
"""
import os


class Env(object):
    """The environment helper.
    """

    def __init__(self, encoding='utf8'):
        """Constructor.
        """
        self.encoding = encoding

    def _get(self, name):
        """Get environment valiable.
        """
        try:
            return os.environ[name].decode(self.encoding)
        except KeyError:
            return ''
