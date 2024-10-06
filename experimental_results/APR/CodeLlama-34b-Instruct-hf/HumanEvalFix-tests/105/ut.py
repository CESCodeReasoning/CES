
from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False

def check(by_length):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"], "Error"
    assert by_length([]) == [], "Error"
    assert by_length([1, -1 , 55]) == ['One'], "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert by_length([1, -1, 3, 2]) == ["Three", "Two", "One"]
    assert by_length([9, 4, 8]) == ["Nine", "Eight", "Four"]

check(by_length)