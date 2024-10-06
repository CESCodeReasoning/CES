from typing import *
import math
def max_fill(grid, capacity):
    return sum([math.ceil(sum(arr)/capacity) for arr in grid])

output = max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1) 
file = open("/home/changshu/CODEMIND/dataset/humaneval/HumanEval_115/output.txt", 'w')
file.write(str(output))
file.close()
    