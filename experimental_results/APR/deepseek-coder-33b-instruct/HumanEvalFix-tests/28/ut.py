
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False

def concatenate(strings: List[str]) -> str:
    if not strings:
        return ''
    return ' '.join(strings)






def check(concatenate):
    assert concatenate([]) == ''
    assert concatenate(['x', 'y', 'z']) == 'xyz'
    assert concatenate(['x', 'y', 'z', 'w', 'k']) == 'xyzwk'

check(concatenate)