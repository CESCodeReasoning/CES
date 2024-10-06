
def how_many_times(string: str, substring: str) -> int:
    times = 0
    start = 0

    while True:
        start = string.find(substring, start)
        if start == -1:
            break
        times += 1
        start += 1

    return times






def check(how_many_times):
    assert how_many_times('', 'x') == 0
    assert how_many_times('xyxyxyx', 'x') == 4
    assert how_many_times('cacacacac', 'cac') == 4
    assert how_many_times('john doe', 'john') == 1

check(how_many_times)