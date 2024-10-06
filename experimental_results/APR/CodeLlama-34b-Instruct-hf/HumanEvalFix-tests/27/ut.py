
def flip_case(string: str) -> str:
    result = ''
    for char in string:
        if char.islower():
            result += char.upper()
        else:
            result += char.lower()
    return result






def check(flip_case):
    assert flip_case('') == ''
    assert flip_case('Hello!') == 'hELLO!'
    assert flip_case('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'

check(flip_case)