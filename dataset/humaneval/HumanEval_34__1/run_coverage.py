from typing import *


def unique(l: list):
    return sorted(list(set(l)))

unique([2, 1, 1, 2, 1, 1])