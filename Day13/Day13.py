print("Exam Grade Calculator")
print()
exam = input("Name of exam:")
print()
max_score = int(input("Max. Possible Score :"))
print()
your_score = int(input("Your score:"))
print()
percentage = (your_score/max_score)*100
print("Your percentage is:", percentage, "%")
print()
if your_score >= 90:
  print("You got", your_score,"%", "which is A+")
elif your_score >= 80 and your_score <= 89:
  print("You got", your_score,"%", "which is A-")
elif your_score >= 70 and your_score <= 79:
  print("You got", your_score,"%", "which is B")
elif your_score >= 60 and your_score <= 69:
  print("You got", your_score,"%", "which is C")
elif your_score >= 50 and your_score <= 59:
  print("You got","%", "which is D")
elif your_score >= 40 and your_score <= 49:
  print("You got","%", "which is U")
else:
  print("Try again!")