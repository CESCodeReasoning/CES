from typing import *


def eat(number, need, remaining):
    if (need <= remaining):
        return [number + need, remaining - need]
    else:
        return [number + remaining, 0]

eat(2, 11, 5)