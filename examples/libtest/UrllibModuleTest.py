# Testing time module

import sys
import UnitTest
import urllib.request, urllib.parse, urllib.error


class UrllibModuleTest(UnitTest.UnitTest):

    def test_quote(self):
        self.assertEqual(urllib.parse.quote("hey"), "hey")
        self.assertEqual(urllib.parse.quote("$%&/?/+ s", safe=""),
                "%24%25%26%2F%3F%2F%2B%20s")

    def test_urlencode(self):
        self.assertEqual(urllib.parse.urlencode({"a": 34, "bbb": "ccc"}),
                "a=34&bbb=ccc")
        self.assertEqual(urllib.parse.urlencode({"a": 34}), "a=34")
        self.assertEqual(urllib.parse.urlencode({}), "")
        self.assertEqual(urllib.parse.urlencode({"a": 34, "bbb": "$%&s"}),
                "a=34&bbb=%24%25%26s")
