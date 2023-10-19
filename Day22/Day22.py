print("Welcome to Guess the Number.")
print()
print("Guess a number between 1 and 10 and I will tell you if you are too low, too high, or get it correct.")
print()
print("Let's Go!!")
import random

attempt = 1
correct_number = random.randint(1,10)
while True:
  user_guess = int(input("Pick a number between 1 and 10: "))
  if user_guess < 0:
    print("Now we'll never know what the answer is …")
    exit()
  if user_guess < correct_number:
    print("That number is too low. Try again!")
    attempt += 1
  elif user_guess > correct_number:
    print("That number is too high. Try again!")
    attempt += 1
    continue
  elif user_guess == correct_number:
    print("You have won! 😍")
    break 
  else:
    print("I don't recognize this number")
print("It took you", attempt, "attempt(s) to get the correct answer. Good One!")