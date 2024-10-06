from typing import *


def sort_third(l: list):
    l = list(l)
    l[::3] = sorted(l[::3])
    return l

sort_third([5, 8, -12, 4, 23, 2, 3, 11, 12, -10])