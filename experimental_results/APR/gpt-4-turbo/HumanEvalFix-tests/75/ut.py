
def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        for j in range(2, int(n**0.5) + 1):  # Start from 2 and go up to the square root of n
            if n % j == 0:
                return False
        return True

    # Since a is less than 100, we only need to consider primes less than 100
    primes = [i for i in range(2, 101) if is_prime(i)]
    for i in primes:
        for j in primes:
            for k in primes:
                if i * j * k == a:
                    return True
    return False

def check(is_multiply_prime):

    assert is_multiply_prime(5) == False
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(8) == True
    assert is_multiply_prime(10) == False
    assert is_multiply_prime(125) == True
    assert is_multiply_prime(3 * 5 * 7) == True
    assert is_multiply_prime(3 * 6 * 7) == False
    assert is_multiply_prime(9 * 9 * 9) == False
    assert is_multiply_prime(11 * 9 * 9) == False
    assert is_multiply_prime(11 * 13 * 7) == True

check(is_multiply_prime)