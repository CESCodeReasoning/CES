
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number = min(numbers)
    max_number = max(numbers)
    range_number = max_number - min_number  # Calculate the range of the numbers
    return [(x - min_number) / range_number for x in numbers]  # Normalize by dividing by the range, not by adding min and max






def check(rescale_to_unit):
    assert rescale_to_unit([2.0, 49.9]) == [0.0, 1.0]
    assert rescale_to_unit([100.0, 49.9]) == [1.0, 0.0]
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit([2.0, 1.0, 5.0, 3.0, 4.0]) == [0.25, 0.0, 1.0, 0.5, 0.75]
    assert rescale_to_unit([12.0, 11.0, 15.0, 13.0, 14.0]) == [0.25, 0.0, 1.0, 0.5, 0.75]

check(rescale_to_unit)