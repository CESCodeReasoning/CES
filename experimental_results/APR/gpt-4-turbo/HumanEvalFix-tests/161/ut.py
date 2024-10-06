
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True
    return False

def solve(s: str) -> str:
    flg = False
    new_str = []
    for i in s:
        if i.isalpha():
            flg = True
            if i.islower():
                new_str.append(i.upper())
            else:
                new_str.append(i.lower())
        else:
            new_str.append(i)
    if not flg:
        return ''.join(new_str[::-1])
    return ''.join(new_str)

# Tests for has_close_elements
def check_has_close_elements(has_close_elements):
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
    assert has_close_elements([1.1, 2.2, 3.1, 4.1, 5.1], 1.0) == True
    assert has_close_elements([1.1, 2.2, 3.1, 4.1, 5.1], 0.5) == False

# Tests for solve
def check_solve(solve):
    assert solve("AsDf") == "aSdF"
    assert solve("1234") == "4321"
    assert solve("ab") == "AB"
    assert solve("#a@C") == "#A@c"
    assert solve("#AsdfW^45") == "#aSDFw^45"
    assert solve("#6@2") == "2@6#"
    assert solve("#$a^D") == "#$A^d"
    assert solve("#ccc") == "#CCC"

def check(solve):

    # Check some simple cases
    assert solve("AsDf") == "aSdF"
    assert solve("1234") == "4321"
    assert solve("ab") == "AB"
    assert solve("#a@C") == "#A@c"
    assert solve("#AsdfW^45") == "#aSDFw^45"
    assert solve("#6@2") == "2@6#"

    # Check some edge cases that are easy to work out by hand.
    assert solve("#$a^D") == "#$A^d"
    assert solve("#ccc") == "#CCC"

    # Don't remove this line:

check(solve)