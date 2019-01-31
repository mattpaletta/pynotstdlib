from typing import Iterable


def avg(lst: Iterable):
    my_sum = 0
    my_len = 0
    # We iterate so that we can use it with generators
    for i in lst:
        my_len += 1
        my_sum += i

    return my_sum / my_len
