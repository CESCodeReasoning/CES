from typing import *	##line:(1)
def search(lst):	##line:(2)
    frq = [0] * (max(lst) + 1)	##line:(3)
    for i in lst:	##line:(4)
        frq[i] += 1;	##line:(5)
	##line:(6)
    ans = -1	##line:(7)
    for i in range(1, len(frq)):	##line:(8)
        if frq[i] >= i:	##line:(9)
            ans = i	##line:(10)
    	##line:(11)
    return ans	##line:(12)

search([5, 5, 5, 5, 1]) 