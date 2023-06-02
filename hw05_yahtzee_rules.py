# Yahtzee Game

import random
# Die class
class Die:
    def __init__(self):
        self.face = None

    def roll(self):
        self.face = random.randint(1, 6)

    def __str__(self):
        return str(self.face)

# Yahtzee Class
class YahtzeeDice:
    def __init__(self):
        self.dices = [Die() for _ in range(5)]

    def roll_dices(self, dices):
        for index in dices:
            self.dices[index-1].roll()

    def show_faces(self):
        for index, die in enumerate(self.dices):
            print(f"주사위 {index+1} 눈: {die.face}")
        print()

    def get_faces(self):
        return [die.face for die in self.dices]

    def count_faces(self, target_face):
        count = 0
        for die in self.dices:
            if die.face == target_face:
                count += 1
        return count

    def sum_faces(self):
        return sum(self.get_faces())

    def __str__(self):
        return ', '.join([str(die.face) for die in
                          self.dices]) + f"\nCounts: {', '.join(str(self.count_faces(i)) for i in range(1, 6))}\nSum: {self.sum_faces()}\n"

from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class Rule(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def points(self, dice):
        pass

    def __str__(self):
        return self.name

class SameValue(Rule):
    def __init__(self, name, value):
        super().__init__(name)
        self.value = value

    def points(self, dice):
        return sum(face for face in dice.get_faces() if face == self.value)

    def __str__(self):
        return f"{self.name} ({self.value})"

class ThreeOfAKind(Rule):
    def __init__(self):
        super().__init__("Three of a Kind")

    def points(self, dice):
        counts = dice.get_faces()
        for face in counts:
            if counts.count(face) >= 3:
                return sum(dice.get_faces())
        return 0

    def __str__(self):
        return self.name

class FourOfAKind(Rule):
    def __init__(self):
        super().__init__("Four of a Kind")

    def points(self, dice):
        counts = dice.get_faces()
        for face in counts:
            if counts.count(face) >= 4:
                return sum(dice.get_faces())
        return 0

    def __str__(self):
        return self.name

class FullHouse(Rule):
    def __init__(self):
        super().__init__("Full House")

    def points(self, dice):
        counts = dice.get_faces()
        if len(set(counts)) == 2 and (counts.count(counts[0]) == 3 or counts.count(counts[0]) == 2):
            return 25
        return 0

    def __str__(self):
        return self.name

class Yahtzee(Rule):
    def __init__(self):
        super().__init__("Yahtzee")

    def points(self, dice):
        counts = dice.get_faces()
        if counts.count(counts[0]) == 5:
            return 50
        return 0

    def __str__(self):
        return self.name

class Chance(Rule):
    def __init__(self):
        super().__init__("Chance")

    def points(self, dice):
        return sum(dice.get_faces())

    def __str__(self):
        return self.name

class Straight(Rule):
    def __init__(self, name, straight):
        super().__init__(name)
        self.straight = straight

    def is_straight(self, faces):
        faces.sort()
        return faces == self.straight

    def points(self, dice):
        if self.is_straight(dice.get_faces()):
            return sum(dice.get_faces())
        return 0

    def __str__(self):
        return self.name

class SmallStraight(Straight):
    def __init__(self):
        super().__init__("Small Straight", [1, 2, 3, 4, 5])

    def __str__(self):
        return self.name

class LargeStraight(Straight):
    def __init__(self):
        super().__init__("Large Straight", [2, 3, 4, 5, 6])

    def __str__(self):
        return self.name





#1. test code
## rules = [Rule]
if __name__ == '__main__':
    y_dice = YahtzeeDice()
    y_dice.roll_dices([1, 2, 3, 4, 5])

    print(y_dice)

    rules = [SameValue('Aces', 1), SameValue('Twos', 2), SameValue('Threes', 3), SameValue('Fours', 4), SameValue('Fives', 5), SameValue('Sixes', 6),
             ThreeOfAKind(), FourOfAKind(), FullHouse(), Yahtzee(), Chance(), SmallStraight(), LargeStraight()]

    for rule in rules:
        print(f"{rule}: {rule.points(y_dice)} points")