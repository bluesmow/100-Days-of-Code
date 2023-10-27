import random, os, time
def rolldice(side):
  result = random.randint(1,side)
  return result

def health():
  healthstat= ((rolldice(6) * rolldice(12))/2) + 10
  return healthstat
  
def strength():
  strengthstat= ((rolldice(6) * rolldice(8))/2) + 12
  return strengthstat

while True:
  print("⚔️ Character Builder ⚔️")
  print()
  name = input("Name your Hero: ")
  typeofhero = input("Choose your hero type(Elf, Wizard ,Human, Orc): ")
  print()
  print(name)
  print("Health ", health())
  print("Strength", strength())
  print()
  print("May you Rise like A true Hero")
  print()
  again = input("Again?: ")
  if again == "no":
    break
  time.sleep(1)
  os.system("clear")
  
