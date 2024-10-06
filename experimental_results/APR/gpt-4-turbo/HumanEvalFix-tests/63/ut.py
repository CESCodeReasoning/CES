
def fibfib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 0  # Corrected to return 0 instead of 1
    if n == 2:
        return 1  # Corrected to return 1 instead of 2
    # Use memoization to improve efficiency
    memo = [0] * (n + 1)
    memo[0], memo[1], memo[2] = 0, 0, 1
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    return memo[n]






def check(fibfib):
    assert fibfib(2) == 1
    assert fibfib(1) == 0
    assert fibfib(5) == 4
    assert fibfib(8) == 24
    assert fibfib(10) == 81
    assert fibfib(12) == 274
    assert fibfib(14) == 927

check(fibfib)