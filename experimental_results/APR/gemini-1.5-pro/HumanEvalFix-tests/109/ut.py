
def move_one_ball(arr):
    if len(arr)==0:
      return True
    sorted_array=sorted(arr)
    for i in range(len(arr)):
        matches=True
        for j in range (len(arr)):
          if arr[(i+j)%len(arr)]!=sorted_array[j]:
            matches=False
        if matches:
          return True
    return False


def check(move_one_ball):

    # Check some simple cases
    assert move_one_ball([3, 4, 5, 1, 2])==True, "This prints if this assert fails 1 (good for debugging!)"
    assert move_one_ball([3, 5, 10, 1, 2])==True
    assert move_one_ball([4, 3, 1, 2])==False
    # Check some edge cases that are easy to work out by hand.
    assert move_one_ball([3, 5, 4, 1, 2])==False, "This prints if this assert fails 2 (also good for debugging!)"
    assert move_one_ball([])==True

check(move_one_ball)