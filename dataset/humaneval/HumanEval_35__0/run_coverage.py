from typing import *


def max_element(l: list):
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m

max_element([-5, 2, 48, 9, 4, 0, 6, 7])