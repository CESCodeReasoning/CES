from typing import *	##line:(1)
def intersperse(numbers: List[int], delimeter: int) -> List[int]:	##line:(2)
    if not numbers:	##line:(3)
        return []	##line:(4)
	##line:(5)
    result = []	##line:(6)
	##line:(7)
    for n in numbers[:-1]:	##line:(8)
        result.append(n)	##line:(9)
        result.append(delimeter)	##line:(10)
	##line:(11)
    result.append(numbers[-1])	##line:(12)
	##line:(13)
    return result	##line:(14)

intersperse([], 7) 