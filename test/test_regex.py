from typing import re
from unittest import TestCase

from pynotstdlib.regex.regex import match


class TestRegex(TestCase):
    def test_empty(self):
        result: re.Match = match(string = "", using = "")
        assert result.groups() == (), "Invalid empty string match"

    def test_entire_string(self):
        result: re.Match = match(string = "abc", using = "abc")
        assert result.groups() == "abc", "Invalid match"
