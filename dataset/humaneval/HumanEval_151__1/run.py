from typing import *
def double_the_difference(lst):
    return sum([i**2 for i in lst if i > 0 and i%2!=0 and "." not in str(i)])

output = double_the_difference([])
file = open("/home/changshu/CODEMIND/dataset/humaneval/HumanEval_151__1/output.txt", 'w')
file.write(str(output))
file.close()
    