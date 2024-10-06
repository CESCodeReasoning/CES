
def is_nested(string):
    balance = 0
    max_depth = 0
    for char in string:
        if char == '[':
            balance += 1
            max_depth = max(max_depth, balance)  # Track maximum depth of nesting
        elif char == ']':
            if balance == 0:
                return False  # More closing brackets than opening
            balance -= 1
    return max_depth > 1 and balance == 0  # True if max depth is more than 1 and all brackets are closed

def check(is_nested):

    # Check some simple cases
    assert is_nested('[[]]') == True, "This prints if this assert fails 1 (good for debugging!)"
    assert is_nested('[]]]]]]][[[[[]') == False
    assert is_nested('[][]') == False
    assert is_nested(('[]')) == False
    assert is_nested('[[[[]]]]') == True
    assert is_nested('[]]]]]]]]]]') == False
    assert is_nested('[][][[]]') == True
    assert is_nested('[[]') == False
    assert is_nested('[]]') == False
    assert is_nested('[[]][[') == True
    assert is_nested('[[][]]') == True

    # Check some edge cases that are easy to work out by hand.
    assert is_nested('') == False, "This prints if this assert fails 2 (also good for debugging!)"
    assert is_nested('[[[[[[[[') == False
    assert is_nested(']]]]]]]]') == False

check(is_nested)