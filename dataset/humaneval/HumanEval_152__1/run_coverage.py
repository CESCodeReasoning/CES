from typing import *


def compare(game, guess):
    return [abs(x - y) for x, y in zip(game, guess)]

compare([0,0,0,0,0,0],[0,0,0,0,0,0])