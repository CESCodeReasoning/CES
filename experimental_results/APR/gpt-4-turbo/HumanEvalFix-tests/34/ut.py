
def unique(l: list):
    return sorted(set(l))  # Use set to remove duplicates and then sort the result






def check(unique):
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

check(unique)