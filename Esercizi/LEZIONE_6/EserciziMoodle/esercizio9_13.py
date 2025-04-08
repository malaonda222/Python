import random

class Dice:
    def __init__(self, sides:int=6):
        self.sides = sides

    def roll_dice(self):
        return random.randint(1, self.sides) 

dice_6 = Dice()
dice_10 = Dice(10)
dice_20 = Dice(20)


print("Lanci del dado a 6 facce:")
for i in range(10):
    print(dice_6.roll_dice())

print("Lanci del dado a 10 facce:")
for i in range(10):
    print(dice_10.roll_dice())

print("Lanci del dado a 20 facce:")
for i in range(10):
    print(dice_20.roll_dice())


    