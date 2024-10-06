
def by_length(arr):
    dic = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    # Filter the array to include only numbers between 1 and 9
    filtered_arr = [num for num in arr if 1 <= num <= 9]
    # Sort the filtered array
    sorted_arr = sorted(filtered_arr)
    # Reverse the sorted array
    reversed_arr = sorted_arr[::-1]
    # Replace each number with its corresponding name
    new_arr = [dic[num] for num in reversed_arr]
    return new_arr

def check(by_length):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"], "Error"
    assert by_length([]) == [], "Error"
    assert by_length([1, -1 , 55]) == ['One'], "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert by_length([1, -1, 3, 2]) == ["Three", "Two", "One"]
    assert by_length([9, 4, 8]) == ["Nine", "Eight", "Four"]

check(by_length)