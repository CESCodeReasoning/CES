from typing import *	##line:(1)
def how_many_times(string: str, substring: str) -> int:	##line:(2)
    times = 0	##line:(3)
	##line:(4)
    for i in range(len(string) - len(substring) + 1):	##line:(5)
        if string[i:i+len(substring)] == substring:	##line:(6)
            times += 1	##line:(7)
	##line:(8)
    return times	##line:(9)

how_many_times('', 'x') 