from typing import *
def sum_to_n(n: int):
    return sum(range(n + 1))

output = sum_to_n(6)
file = open("/home/changshu/CODEMIND/dataset/humaneval/HumanEval_60__0/output.txt", 'w')
file.write(str(output))
file.close()
    