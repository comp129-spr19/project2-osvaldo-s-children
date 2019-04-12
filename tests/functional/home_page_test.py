import unittest

from functional_lib.general import get_chromedriver
from functional_lib.general import kill_server
from functional_lib.general import LOCAL_HOST
from functional_lib.general import run_server


class TestStringMethods(unittest.TestCase):

    def test_home_page_layout(self):
        proc = run_server()

        chrome = get_chromedriver()
        chrome.implicitly_wait(30)
        chrome.maximize_window()

        chrome.get(LOCAL_HOST)

        en = chrome.findElementById("events_needs_button")
        self.assertFalse(en is None)

        mp = chrome.findElementById("map_page_button")
        self.assertFalse(mp is None)

        kill_server(proc)


if __name__ == '__main__':
    unittest.main()