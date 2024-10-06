
def is_nested(string):
    cnt = 0
    maximum = 0
    for i in string:
        if i == "[":
            cnt += 1
            maximum = max(cnt, maximum)
        elif i == "]":
            cnt -= 1
    if maximum >= 2:
        return True
    else:
        return False

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