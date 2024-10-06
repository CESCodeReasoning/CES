
from typing import List

def factorize(n: int) -> List[int]:
    import math
    factors = []
    # Check for number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # n must be odd at this point, thus a skip of 2 (i.e., 3, 5, 7, 9,...) is sufficient
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        # While i divides n, append i and divide n
        while n % i == 0:
            factors.append(i)
            n //= i
    # Condition if n is a prime number greater than 2
    if n > 1:
        factors.append(n)
    return factors






def check(factorize):
    assert factorize(2) == [2]
    assert factorize(4) == [2, 2]
    assert factorize(8) == [2, 2, 2]
    assert factorize(3 * 19) == [3, 19]
    assert factorize(3 * 19 * 3 * 19) == [3, 3, 19, 19]
    assert factorize(3 * 19 * 3 * 19 * 3 * 19) == [3, 3, 3, 19, 19, 19]
    assert factorize(3 * 19 * 19 * 19) == [3, 19, 19, 19]
    assert factorize(3 * 2 * 3) == [2, 3, 3]

check(factorize)