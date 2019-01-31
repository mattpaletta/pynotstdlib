from unittest import TestCase

from pynotstdlib.collection.merge import merge_lists


class TestMerge(TestCase):
    def test_empty_list(self):
        result = merge_lists(original = [], new_changes = [])
        assert result == [], "Empty list is the same."

    def test_same_list(self):
        result = merge_lists(original = ["abc", "def"], new_changes = ["abc", "def"])
        assert result == ["abc", "def"], "Single list is the same."

    def test_single_change(self):
        result = merge_lists(original = ["abc", "def"], new_changes = ["abc", "123"])
        assert result == ["abc", "123"], "Changes should have been overwritten, the same has stayed."

    def test_empty_merge(self):
        result = merge_lists(original = [None, "def"], new_changes = ["abc", "def"])
        assert result == ["abc", "def"], "A merge should fill the empty spot from original, " \
                                         "the rest should stay the same."

    def test_merge_shorter(self):
        result = merge_lists(original = ["abc", "def", "ghi"], new_changes = ["123", "456"])
        assert result == ["123", "456", "ghi"], "If merging a shorter list with a longer one " \
                                                "should keep the tail of original"

    def test_merge_longer(self):
        result = merge_lists(original = ["123", "456"], new_changes = ["abc", "def", "ghi"])
        assert result == ["abc", "def", "ghi"], "Merging longer tail should keep the new tail, " \
                                                "replacing any values in the middle"
