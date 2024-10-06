
def is_palindrome(text: str) -> bool:
    for i in range(len(text) // 2):  # Only need to check up to the middle of the string
        if text[i] != text[len(text) - 1 - i]:  # Correct the index for comparison
            return False
    return True

# Tests
def check_is_palindrome(is_palindrome):
    assert is_palindrome('') == True
    assert is_palindrome('aba') == True
    assert is_palindrome('aaaaa') == True
    assert is_palindrome('zbcd') == False
    assert is_palindrome('xywyx') == True
    assert is_palindrome('xywyz') == False
    assert is_palindrome('xywzx') == False

check_is_palindrome(is_palindrome)






def check(is_palindrome):
    assert is_palindrome('') == True
    assert is_palindrome('aba') == True
    assert is_palindrome('aaaaa') == True
    assert is_palindrome('zbcd') == False
    assert is_palindrome('xywyx') == True
    assert is_palindrome('xywyz') == False
    assert is_palindrome('xywzx') == False

check(is_palindrome)