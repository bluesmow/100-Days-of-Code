print("⚔️ Character Stats Generator ⚔️")
import random
def rolldice(sides):
  output = random.randint(1,sides)
  return output
def roll6and8():
  roll6side = rolldice(6)
  roll8side =rolldice(8)
  hps = roll6side * roll8side
  return hps

haveacharacter = "yes"
while haveacharacter == "yes":
  character = input("Name your warior: ")
  hps = str(roll6and8())
  print("Theri health is", hps,"hp")