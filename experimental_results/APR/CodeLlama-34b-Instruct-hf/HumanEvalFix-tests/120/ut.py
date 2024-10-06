
from typing import List

def maximum(arr: List[int], k: int) -> List[int]:
    # Check if the input array is empty or the value of k is invalid
    if not arr or k <= 0 or k > len(arr):
        return []

    # Sort the input array in descending order
    arr.sort(reverse=True)

    # Return the first k elements of the sorted array
    return arr[:k]

def check(maximum):

    # Check some simple cases
    assert maximum([-3, -4, 5], 3) == [-4, -3, 5]
    assert maximum([4, -4, 4], 2) == [4, 4]
    assert maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2]
    assert maximum([123, -123, 20, 0 , 1, 2, -3], 3) == [2, 20, 123]
    assert maximum([-123, 20, 0 , 1, 2, -3], 4) == [0, 1, 2, 20]
    assert maximum([5, 15, 0, 3, -13, -8, 0], 7) == [-13, -8, 0, 0, 3, 5, 15]
    assert maximum([-1, 0, 2, 5, 3, -10], 2) == [3, 5]
    assert maximum([1, 0, 5, -7], 1) == [5]
    assert maximum([4, -4], 2) == [-4, 4]
    assert maximum([-10, 10], 2) == [-10, 10]

    # Check some edge cases that are easy to work out by hand.
    assert maximum([1, 2, 3, -23, 243, -400, 0], 0) == []

check(maximum)