from typing import *
def make_a_pile(n):
    return [n + 2*i for i in range(n)]

output = make_a_pile(6)
file = open("/home/changshu/CODEMIND/dataset/humaneval/HumanEval_100__1/output.txt", 'w')
file.write(str(output))
file.close()
    