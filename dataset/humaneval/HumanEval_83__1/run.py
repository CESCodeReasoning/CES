from typing import *
def starts_one_ends(n):
    if n == 1: return 1
    return 18 * (10 ** (n - 2))

output = starts_one_ends(2)
file = open("/home/changshu/CODEMIND/dataset/humaneval/HumanEval_83__1/output.txt", 'w')
file.write(str(output))
file.close()
    