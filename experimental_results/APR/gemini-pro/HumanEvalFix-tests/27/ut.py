
def flip_case(string: str) -> str:
    flipped_string = ""
    for char in string:
        if char.islower():
            flipped_string += char.upper()
        else:
            flipped_string += char.lower()
    return flipped_string






def check(flip_case):
    assert flip_case('') == ''
    assert flip_case('Hello!') == 'hELLO!'
    assert flip_case('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'

check(flip_case)