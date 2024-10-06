from typing import *	##line:(1)
def largest_prime_factor(n: int):	##line:(2)
    def is_prime(k):	##line:(3)
        if k < 2:	##line:(4)
            return False	##line:(5)
        for i in range(2, k - 1):	##line:(6)
            if k % i == 0:	##line:(7)
                return False	##line:(8)
        return True	##line:(9)
    largest = 1	##line:(10)
    for j in range(2, n + 1):	##line:(11)
        if n % j == 0 and is_prime(j):	##line:(12)
            largest = max(largest, j)	##line:(13)
    return largest	##line:(14)

largest_prime_factor(15) 