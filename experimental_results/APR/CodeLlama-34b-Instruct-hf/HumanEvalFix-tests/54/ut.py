
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False

def same_chars(s0: str, s1: str):
    return all(c in s1 for c in s0) and all(c in s0 for c in s1)






def check(same_chars):
    assert same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc') == True
    assert same_chars('abcd', 'dddddddabc') == True
    assert same_chars('dddddddabc', 'abcd') == True
    assert same_chars('eabcd', 'dddddddabc') == False
    assert same_chars('abcd', 'dddddddabcf') == False
    assert same_chars('eabcdzzzz', 'dddzzzzzzzddddabc') == False
    assert same_chars('aabb', 'aaccc') == False

check(same_chars)