
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False

def truncate_number(number: float) -> float:
    return number - int(number)






def check(truncate_number):
    assert truncate_number(3.5) == 0.5
    assert abs(truncate_number(1.33) - 0.33) < 1e-6
    assert abs(truncate_number(123.456) - 0.456) < 1e-6

check(truncate_number)