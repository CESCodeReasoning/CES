from typing import *
def add(x: int, y: int):
    return x + y

output = add(0, 1) 
file = open("/home/changshu/CODEMIND/dataset/humaneval/HumanEval_53/output.txt", 'w')
file.write(str(output))
file.close()
    