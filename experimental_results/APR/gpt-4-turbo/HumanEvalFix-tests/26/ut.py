
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    from collections import Counter
    count = Counter(numbers)
    return [num for num in numbers if count[num] == 1]  # Check if count is exactly 1 to include the number






def check(remove_duplicates):
    assert remove_duplicates([]) == []
    assert remove_duplicates([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert remove_duplicates([1, 2, 3, 2, 4, 3, 5]) == [1, 4, 5]

check(remove_duplicates)