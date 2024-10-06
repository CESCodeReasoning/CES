
from typing import List
import math

def max_fill(grid: List[List[int]], capacity: int) -> int:
    # Initialize the number of times the buckets are lowered to 0
    num_lowered = 0

    # Loop through each row of the grid
    for row in grid:
        # Initialize the total amount of water in the row to 0
        total_water = 0

        # Loop through each column of the row
        for col in row:
            # If the current cell is a well (represented by a 1), add the capacity of the bucket to the total amount of water
            if col == 1:
                total_water += capacity

        # If the total amount of water in the row is greater than the capacity of the bucket, lower the bucket the necessary number of times
        if total_water > capacity:
            num_lowered += math.floor(total_water / capacity)

    # Return the number of times the buckets are lowered
    return num_lowered

def check(max_fill):


    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1) == 6, "Error"
    assert max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2) == 5, "Error"
    assert max_fill([[0,0,0], [0,0,0]], 5) == 0, "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert max_fill([[1,1,1,1], [1,1,1,1]], 2) == 4, "Error"
    assert max_fill([[1,1,1,1], [1,1,1,1]], 9) == 2, "Error"

check(max_fill)