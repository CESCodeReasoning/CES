
from typing import List

def concatenate(strings: List[str]) -> str:
    return ''.join(strings)  # Remove space to concatenate without spaces

# Tests
def check_concatenate(concatenate):
    assert concatenate([]) == ''
    assert concatenate(['x', 'y', 'z']) == 'xyz'
    assert concatenate(['x', 'y', 'z', 'w', 'k']) == 'xyzwk'

check_concatenate(concatenate)






def check(concatenate):
    assert concatenate([]) == ''
    assert concatenate(['x', 'y', 'z']) == 'xyz'
    assert concatenate(['x', 'y', 'z', 'w', 'k']) == 'xyzwk'

check(concatenate)