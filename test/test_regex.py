from unittest import TestCase

from pynotstdlib.regex.regex import match, search


class TestRegex(TestCase):
    def test_empty_match(self):
        result = match(string = "", using = "")
        assert result.groups() == (), "Invalid empty string match"

    def test_search(self):
        result = search(string = 'abcdef', using = '(?<=abc)def')
        assert result.group(0) == "def", "Invalid match"
