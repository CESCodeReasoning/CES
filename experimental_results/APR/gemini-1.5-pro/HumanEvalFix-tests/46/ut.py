
def fib4(n: int):
    results = [0, 0, 2, 0]
    if n < 4:
        return results[n]

    for i in range(4, n + 1):
        results.append(results[i-1] + results[i-2] + results[i-3] + results[i-4])
    
    return results[n]






def check(fib4):
    assert fib4(5) == 4
    assert fib4(8) == 28
    assert fib4(10) == 104
    assert fib4(12) == 386

check(fib4)