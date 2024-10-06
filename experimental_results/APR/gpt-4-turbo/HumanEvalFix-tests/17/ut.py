
from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map = {'o': 4, 'o|': 2, '.|': 1}  # Correct the mapping values for 'o' and 'o|'
    notes = music_string.split()
    result = []
    for note in notes:
        if note in note_map:
            result.append(note_map[note])
        else:
            result.append(4)  # Default to 4 beats for 'o' without '|'
    return result






def check(parse_music):
    assert parse_music('') == []
    assert parse_music('o o o o') == [4, 4, 4, 4]
    assert parse_music('.| .| .| .|') == [1, 1, 1, 1]
    assert parse_music('o| o| .| .| o o o o') == [2, 2, 1, 1, 4, 4, 4, 4]
    assert parse_music('o| .| o| .| o o| o o|') == [2, 1, 2, 1, 4, 2, 4, 2]

check(parse_music)