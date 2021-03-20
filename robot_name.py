from random import choices
from string import ascii_uppercase, digits


class Robot:
    def __init__(self):
        self.name = ''
        self.name2 = []

        self.reset()

    def reset(self):
        while True:
            self.name = ''.join(choices(ascii_uppercase, k=2) + choices(digits, k=3))
            if self.name not in self.name2:
                self.name2.append(self.name)
                break


# robot = Robot()
# print(robot.result)
# print(robot.name)