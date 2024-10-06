from typing import *
def change_base(x: int, base: int):
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret

output = change_base(234, 2)
file = open("/home/changshu/CODEMIND/dataset/humaneval/HumanEval_44__0/output.txt", 'w')
file.write(str(output))
file.close()
    