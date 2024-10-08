from typing import *
def prod_signs(arr):
    if not arr: return None
    prod = 0 if 0 in arr else (-1) ** len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])

output = prod_signs([1, 1, 1, 2, 3, -1, 1])
file = open("/home/changshu/CODEMIND/dataset/humaneval/HumanEval_128__1/output.txt", 'w')
file.write(str(output))
file.close()
    