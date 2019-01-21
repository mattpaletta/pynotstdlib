import re
from threadlru import LRUCache
regex_strings = LRUCache(max_size = 20)
regex_answers = LRUCache(max_size = 30)


def match(string: str, using: str):
    # Automatically compiles and matches the regex string provided.
    # Stores 20 compiled strings, and 30 'matches'.
    my_regex = regex_strings.compute_if_not_exists(key = using, fun = re.compile)
    return regex_answers.compute_if_not_exists(key = string + my_regex, fun = lambda: re.match(my_regex, string))
