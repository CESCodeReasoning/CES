
def move_one_ball(arr):
    if len(arr) == 0:
        return True
    sorted_array = sorted(arr)
    
    # Find the index of the smallest element in the original array
    min_index = arr.index(sorted_array[0])
    
    # Rotate the array from the min_index
    my_arr = arr[min_index:] + arr[:min_index]
    
    # Check if the rotated array matches the sorted array
    return my_arr == sorted_array

def check(move_one_ball):

    # Check some simple cases
    assert move_one_ball([3, 4, 5, 1, 2])==True, "This prints if this assert fails 1 (good for debugging!)"
    assert move_one_ball([3, 5, 10, 1, 2])==True
    assert move_one_ball([4, 3, 1, 2])==False
    # Check some edge cases that are easy to work out by hand.
    assert move_one_ball([3, 5, 4, 1, 2])==False, "This prints if this assert fails 2 (also good for debugging!)"
    assert move_one_ball([])==True

check(move_one_ball)