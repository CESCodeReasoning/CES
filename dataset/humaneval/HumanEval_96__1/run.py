from typing import *
def count_up_to(n):
    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes


output = count_up_to(22)
file = open("/home/changshu/CODEMIND/dataset/humaneval/HumanEval_96__1/output.txt", 'w')
file.write(str(output))
file.close()
    