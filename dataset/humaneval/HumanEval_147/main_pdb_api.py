from typing import *	##line:(1)
def get_max_triples(n):	##line:(2)
    A = [i*i - i + 1 for i in range(1,n+1)]	##line:(3)
    ans = []	##line:(4)
    for i in range(n):	##line:(5)
        for j in range(i+1,n):	##line:(6)
            for k in range(j+1,n):	##line:(7)
                if (A[i]+A[j]+A[k])%3 == 0:	##line:(8)
                    ans += [(A[i],A[j],A[k])]	##line:(9)
    return len(ans)	##line:(10)

get_max_triples(5) 