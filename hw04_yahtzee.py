# Yahtzee Game
import random
# Die class
class Die():
    def __init__(self, face):
        self.face = _face

    @property
    def face(self):
        return random.randint(1,6)

    def roll(self):  None