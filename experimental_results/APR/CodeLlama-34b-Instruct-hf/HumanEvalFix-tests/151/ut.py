
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False

def double_the_difference(lst):
    odd_sum = sum([i**2 for i in lst if i%2!=0 and i > 0])
    return odd_sum

def check(double_the_difference):

    # Check some simple cases
    assert double_the_difference([]) == 0 , "This prints if this assert fails 1 (good for debugging!)"
    assert double_the_difference([5, 4]) == 25 , "This prints if this assert fails 2 (good for debugging!)"
    assert double_the_difference([0.1, 0.2, 0.3]) == 0 , "This prints if this assert fails 3 (good for debugging!)"
    assert double_the_difference([-10, -20, -30]) == 0 , "This prints if this assert fails 4 (good for debugging!)"


    # Check some edge cases that are easy to work out by hand.
    assert double_the_difference([-1, -2, 8]) == 0, "This prints if this assert fails 5 (also good for debugging!)"
    assert double_the_difference([0.2, 3, 5]) == 34, "This prints if this assert fails 6 (also good for debugging!)"
    lst = list(range(-99, 100, 2))
    odd_sum = sum([i**2 for i in lst if i%2!=0 and i > 0])
    assert double_the_difference(lst) == odd_sum , "This prints if this assert fails 7 (good for debugging!)"

check(double_the_difference)