from typing import *	##line:(1)
def even_odd_count(num):	##line:(2)
    even_count = 0	##line:(3)
    odd_count = 0	##line:(4)
    for i in str(abs(num)):	##line:(5)
        if int(i)%2==0:	##line:(6)
            even_count +=1	##line:(7)
        else:	##line:(8)
            odd_count +=1	##line:(9)
    return (even_count, odd_count)	##line:(10)

even_odd_count(7) 