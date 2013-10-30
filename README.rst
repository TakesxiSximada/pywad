The Python Web Auto Drive Framework.

The pywad is framework for driving the web browser automatically,
using selenium. Need Selenium and python binding of it(selenium-2.35.0 or later).
And need the Chrome Driver if you want to be use Google Chrome.
But we have not been able to support it not yet.
Now, Firefox only.

install
===========

Need Selenium,
see http://www.seleniumhq.org/

Next, execute command.::

    $ pip install pywad


How to use
===========

The pywad.Part control the browser when pywad.Part.is_target() return True.
:term:`browser` is a selenium's WebDriver object. :term:`status` is a dictionaly,
but anything ok. The mission of it is to communicate datas for other part object.

For example,
::

    from pywad import Part
    from pywad.decorator import url_match
    
    class GoogleTop(Part):

        @url_match('www\.google\.')
        def is_target(self, browser, status):
            return True

        def run(self, browser, status):
            entries = browser.find_elements_by_css_selector('input')
            for entry in entries:
                if entry.get_attribute('type') == 'text':
                    entry.send_keys('test\n\n')

        def _is_search_button(self, text):
            for word in self.search_words:
                if word in text:
                    return True

Next, let running it using Runner object. The Runner object is list-like object.
It expects that the Part object enters. Run the parts objects if execute Runner.run().

::

    def main():
        url = 'http://www.google.com'
        runner = Runner()
        runner.append(GoogleTop())
        runner.run(url)

    if __name__ == '__main__':
        main()
