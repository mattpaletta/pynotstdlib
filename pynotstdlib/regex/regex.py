import re
from threadlru import LRUCache
regex_strings = LRUCache(max_size = 20)
regex_answers = LRUCache(max_size = 30)


def match(string: str, using: str):
    # Automatically compiles and matches the regex string provided.
    # Stores 20 compiled strings, and 30 'matches'.
    my_regex = regex_strings.compute_if_not_exists(key = using, fun = re.compile, pattern = using)
    return regex_answers.compute_if_not_exists(key = string + using + "match", fun = lambda: re.match(my_regex, string))


def findall(string: str, using: str):
    # Automatically compiles and matches the regex string provided.
    # Stores 20 compiled strings, and 30 'matches'.
    my_regex = regex_strings.compute_if_not_exists(key = using, fun = re.compile, pattern = using)
    return regex_answers.compute_if_not_exists(key = string + using + "findall", fun = lambda: re.findall(my_regex, string))


def search(string: str, using: str):
    # Automatically compiles and matches the regex string provided.
    # Stores 20 compiled strings, and 30 'matches'.
    my_regex = regex_strings.compute_if_not_exists(key = using, fun = re.compile, pattern = using)
    return regex_answers.compute_if_not_exists(key = string + using + "search", fun = lambda: re.search(my_regex, string))
