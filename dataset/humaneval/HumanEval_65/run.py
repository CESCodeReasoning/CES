from typing import *
def circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]

output = circular_shift(100, 2) 
file = open("/home/changshu/CODEMIND/dataset/humaneval/HumanEval_65/output.txt", 'w')
file.write(str(output))
file.close()
    