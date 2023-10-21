print("Infinity Dice 🎲")
print()
import random

side = int(input("How many sides: "))
numberoftimesrolled = random.randint(1, side)
playgame ="yes"
def diceroll(side):
  print("You rolled", numberoftimesrolled)
while playgame == "yes":
  diceroll(side)
  playgame = input("Roll again?")