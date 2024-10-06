
def closest_integer(value):
    from math import floor, ceil

    # Remove trailing zeros
    while value[-1] == '0':
        value = value[:-1]

    # Convert the string to a float
    num = float(value)

    # Check if the number is equidistant from two integers
    if value[-2:] == '.5':
        # Round the number away from zero
        if num > 0:
            res = floor(num)
        else:
            res = ceil(num)
    # If the number is not equidistant from two integers, round it to the nearest integer
    else:
        res = int(round(num))

    return res

def check(closest_integer):

    # Check some simple cases
    assert closest_integer("10") == 10, "Test 1"
    assert closest_integer("14.5") == 15, "Test 2"
    assert closest_integer("-15.5") == -16, "Test 3"
    assert closest_integer("15.3") == 15, "Test 3"

    # Check some edge cases that are easy to work out by hand.
    assert closest_integer("0") == 0, "Test 0"

check(closest_integer)