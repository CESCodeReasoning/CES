from typing import *


def same_chars(s0: str, s1: str):
    return set(s0) == set(s1)

same_chars('eabcd', 'dddddddabc')