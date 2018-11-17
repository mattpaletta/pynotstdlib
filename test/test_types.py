from unittest import TestCase

from pynotstdlib.types import is_int, is_int_strict, is_bool


class TestPQDict(TestCase):
    def test_int(self):
        assert is_int(1), "1 is an int"

    def test_int_strict(self):
        assert not is_int(1.0, strict = True), "1.0 is not an int strict"
        assert not is_int_strict(1.0), "1.0 is not an int strict"

    def test_bool(self):
        assert is_bool(True), "True is a boolean"

    def test_bool_int(self):
        assert is_bool(1, strict = False), "1 can be interpreted as a boolean"
