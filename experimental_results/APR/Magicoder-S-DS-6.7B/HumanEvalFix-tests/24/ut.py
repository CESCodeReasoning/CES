
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True






def check(largest_divisor):
    assert largest_divisor(3) == 1
    assert largest_divisor(7) == 1
    assert largest_divisor(10) == 5
    assert largest_divisor(100) == 50
    assert largest_divisor(49) == 7

check(largest_divisor)