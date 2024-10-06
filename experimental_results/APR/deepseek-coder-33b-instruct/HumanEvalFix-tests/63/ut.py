
def fibfib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    fibfib_sequence = [0, 0, 1]
    for i in range(3, n+1):
        fibfib_sequence.append(fibfib_sequence[i-1] + fibfib_sequence[i-2] + fibfib_sequence[i-3])
    return fibfib_sequence[n]






def check(fibfib):
    assert fibfib(2) == 1
    assert fibfib(1) == 0
    assert fibfib(5) == 4
    assert fibfib(8) == 24
    assert fibfib(10) == 81
    assert fibfib(12) == 274
    assert fibfib(14) == 927

check(fibfib)