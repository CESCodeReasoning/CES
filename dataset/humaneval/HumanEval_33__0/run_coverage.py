from typing import *


def sort_third(l: list):
    l = list(l)
    l[::3] = sorted(l[::3])
    return l

sort_third([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])