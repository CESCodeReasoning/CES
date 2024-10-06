from typing import *


def can_arrange(arr):
    ind = -1
    i = 1
    print(len(arr))
    while i < len(arr):
        if arr[i] < arr[i - 1]:
            ind = i
        i += 1
    return ind

can_arrange([4,8,5,7,3])