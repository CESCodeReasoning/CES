from typing import *	##line:(1)
def hex_key(num):	##line:(2)
    primes = ('2', '3', '5', '7', 'B', 'D')	##line:(3)
    total = 0	##line:(4)
    for i in range(0, len(num)):	##line:(5)
        if num[i] in primes:	##line:(6)
            total += 1	##line:(7)
    return total	##line:(8)

hex_key("AB") 