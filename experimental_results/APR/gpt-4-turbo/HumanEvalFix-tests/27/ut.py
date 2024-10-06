
def flip_case(string: str) -> str:
    flipped = []
    for char in string:
        if char.islower():
            flipped.append(char.upper())
        else:
            flipped.append(char.lower())
    return ''.join(flipped)






def check(flip_case):
    assert flip_case('') == ''
    assert flip_case('Hello!') == 'hELLO!'
    assert flip_case('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'

check(flip_case)