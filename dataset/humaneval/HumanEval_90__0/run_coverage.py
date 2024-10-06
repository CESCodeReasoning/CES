from typing import *


def next_smallest(lst):
    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]

next_smallest([5, 1, 4, 3, 2])