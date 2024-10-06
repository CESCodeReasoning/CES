from typing import *


def solution(lst):
    return sum([x for idx, x in enumerate(lst) if idx % 2 == 0 and x % 2 == 1])

solution([30, 13, 23, 32])