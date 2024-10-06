
def total_match(lst1, lst2):
    l1 = sum(len(st) for st in lst1)  # Calculate total length of strings in lst1
    l2 = sum(len(st) for st in lst2)  # Calculate total length of strings in lst2
    
    if l1 < l2:
        return lst1
    elif l2 < l1:
        return lst2
    else:
        return lst1  # Return lst1 if both have the same total number of characters

# Tests for total_match

def check(total_match):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert total_match([], []) == []
    assert total_match(['hi', 'admin'], ['hi', 'hi']) == ['hi', 'hi']
    assert total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
    assert total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']
    assert total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
    assert total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
    assert total_match(['hi', 'admin'], ['hI', 'hi', 'hii']) == ['hi', 'admin']


    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert total_match([], ['this']) == []
    assert total_match(['this'], []) == []

check(total_match)