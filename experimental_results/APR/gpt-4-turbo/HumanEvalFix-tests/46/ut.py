
def fib4(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    results = [0, 0, 2, 0]  # Correct initial values for fib4 sequence
    for _ in range(4, n + 1):
        next_value = results[-1] + results[-2] + results[-3] + results[-4]
        results.append(next_value)
        results.pop(0)  # Maintain the last four results

    return results[-1]  # Return the last element which is fib4(n)






def check(fib4):
    assert fib4(5) == 4
    assert fib4(8) == 28
    assert fib4(10) == 104
    assert fib4(12) == 386

check(fib4)