
def is_nested(string):
    stack = []
    for bracket in string:
        if bracket == '[':
            stack.append(bracket)
        elif bracket == ']':
            if len(stack) > 1 and stack[-2] == '[':
                return True
            else:
                stack.pop()
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