from typing import *


def pluck(arr):
    if (len(arr) == 0):
        return []
    evens = list(filter(lambda x: x % 2 == 0, arr))
    if (evens == []):
        return []
    return [min(evens), arr.index(min(evens))]

pluck([5, 0, 3, 0, 4, 2])