from random import choices, seed
from string import ascii_uppercase, digits


class Robot:
    def __init__(self):
        self.name = draw()

    def reset(self):
        self.__init__()


def draw():
    seed()
    return ''.join(choices(ascii_uppercase, k=2) + choices(digits, k=3))