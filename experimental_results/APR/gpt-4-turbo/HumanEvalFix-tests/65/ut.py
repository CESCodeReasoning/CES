
def circular_shift(x, shift):
    s = str(x)
    shift = shift % len(s)  # Use modulo to handle shifts larger than the number of digits
    if shift == 0:
        return s
    else:
        return s[-shift:] + s[:-shift]  # Correctly perform the circular shift

def check(circular_shift):

    # Check some simple cases
    assert circular_shift(100, 2) == "001"
    assert circular_shift(12, 2) == "12"
    assert circular_shift(97, 8) == "79"
    assert circular_shift(12, 1) == "21", "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert circular_shift(11, 101) == "11", "This prints if this assert fails 2 (also good for debugging!)"

check(circular_shift)