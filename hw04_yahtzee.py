# Yahtzee Game

import random
# Die class
class Die:
    def __init__(self):
        self.face = None

    def roll(self):
        self.face = random.randint(1, 6)

    def __str__(self):
        return f'Dice face : {self.face}'

# Yahtzee Class
class Yahtzee:
    def __init__(self):
        self.dice = [Die for _ in range(5)]