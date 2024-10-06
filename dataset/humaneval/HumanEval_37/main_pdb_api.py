from typing import *	##line:(1)
def sort_even(l: list):	##line:(2)
    evens = l[::2]	##line:(3)
    odds = l[1::2]	##line:(4)
    evens.sort()	##line:(5)
    ans = []	##line:(6)

    for e, o in zip(evens, odds):	##line:(7)
        ans.extend([e, o])	##line:(8)
    if len(evens) > len(odds):	##line:(9)
        ans.append(evens[-1])	##line:(10)
    return ans	##line:(11)

tuple(sort_even([1, 2, 3]))