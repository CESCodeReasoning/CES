from typing import *
def minSubArraySum(nums):
    max_sum = 0
    s = 0
    for num in nums:
        s += -num
        if (s < 0):
            s = 0
        max_sum = max(s, max_sum)
    if max_sum == 0:
        max_sum = max(-i for i in nums)
    min_sum = -max_sum
    return min_sum

output = minSubArraySum([2, 3, 4, 1, 2, 4]) 
file = open("/home/changshu/CODEMIND/dataset/humaneval/HumanEval_114/output.txt", 'w')
file.write(str(output))
file.close()
    