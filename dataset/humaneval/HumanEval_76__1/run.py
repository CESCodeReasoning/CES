from typing import *
def is_simple_power(x, n):
    if (n == 1): 
        return (x == 1) 
    power = 1
    while (power < x): 
        power = power * n 
    return (power == x) 

output = is_simple_power(128, 4)
file = open("/home/changshu/CODEMIND/dataset/humaneval/HumanEval_76__1/output.txt", 'w')
file.write(str(output))
file.close()
    