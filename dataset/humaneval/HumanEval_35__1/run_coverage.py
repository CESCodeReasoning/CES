from typing import *


def max_element(l: list):
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m

max_element([3, 2, -3.5, 0])