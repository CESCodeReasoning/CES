from typing import *
def string_sequence(n: int) -> str:
    return ' '.join([str(x) for x in range(n + 1)])

output = string_sequence(10)
file = open("/home/changshu/CODEMIND/dataset/humaneval/HumanEval_15__1/output.txt", 'w')
file.write(str(output))
file.close()
    