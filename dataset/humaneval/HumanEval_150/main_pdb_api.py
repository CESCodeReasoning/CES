from typing import *	##line:(1)
def x_or_y(n, x, y):	##line:(2)
    if n == 1:	##line:(3)
        return y	##line:(4)
    for i in range(2, n):	##line:(5)
        if n % i == 0:	##line:(6)
            return y	##line:(7)
            break	##line:(8)
    else:	##line:(9)
        return x	##line:(10)

x_or_y(7, 34, 12) 