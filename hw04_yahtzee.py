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

    def roll_dices(self, dice_indices):
        for index in dice_indices:
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


if __name__ == '__main__':
    y_dice = YahtzeeDice()
    y_dice.roll_dices([1,2,3,4,5])

    print(y_dice)





