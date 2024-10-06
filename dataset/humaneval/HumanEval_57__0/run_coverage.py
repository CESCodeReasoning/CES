from typing import *


def monotonic(l: list):
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False

monotonic([4, 1, 0, -10])