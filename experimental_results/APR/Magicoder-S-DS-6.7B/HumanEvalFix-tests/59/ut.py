
def is_palindrome(s: str) -> bool:
    s = s.lower()
    s = ''.join(e for e in s if e.isalnum())
    return s == s[::-1]






def check(largest_prime_factor):
    assert largest_prime_factor(15) == 5
    assert largest_prime_factor(27) == 3
    assert largest_prime_factor(63) == 7
    assert largest_prime_factor(330) == 11
    assert largest_prime_factor(13195) == 29

check(largest_prime_factor)