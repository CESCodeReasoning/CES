from typing import *


def maximum(arr, k):
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans

maximum([123, -123, 20, 0 , 1, 2, -3], 3)