#! /usr/bin/env python
#-*- coding: utf-8 -*-

from pywad import Runner, Part, url_match

class GoogleTop(Part):
    def _is_search_button(self, text):
        for word in self.search_words:
            if word in text:
                return True

    @url_match('www\.google\.')
    def is_target(self, browser, status):
        return True

    def run(self, browser, status):
        entries = browser.find_elements_by_css_selector('input')
        for entry in entries:
            if entry.get_attribute('type') == 'text':
                entry.send_keys('test\n\n')

def main():
    url = 'http://www.google.com'
    runner = Runner()
    runner.append(GoogleTop())
    runner.run(url)

if __name__ == '__main__':
    main()
