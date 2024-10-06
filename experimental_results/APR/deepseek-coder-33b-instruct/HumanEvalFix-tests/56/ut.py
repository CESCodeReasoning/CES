
from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False

def correct_bracketing(brackets: str) -> bool:
    depth = 0
    for b in brackets:
        if b == ">":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0






def check(correct_bracketing):
    assert correct_bracketing("<>")
    assert correct_bracketing("<<><>>")
    assert correct_bracketing("<><><<><>><>")
    assert correct_bracketing("<><><<<><><>><>><<><><<>>>")
    assert not correct_bracketing("<<<><>>>>")
    assert not correct_bracketing("><<>")
    assert not correct_bracketing("<")
    assert not correct_bracketing("<<<<")
    assert not correct_bracketing(">")
    assert not correct_bracketing("<<>")
    assert not correct_bracketing("<><><<><>><>><<>")
    assert not correct_bracketing("<><><<><>><>>><>")

check(correct_bracketing)