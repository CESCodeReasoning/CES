from typing import *
def unique_digits(x):
    odd_digit_elements = []
    for i in x:
        if all (int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)

output = unique_digits([12345, 2033, 111, 151])
file = open("/home/changshu/CODEMIND/dataset/humaneval/HumanEval_104__1/output.txt", 'w')
file.write(str(output))
file.close()
    