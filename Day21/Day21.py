print("Math Game!")
print()
multiples = int(input("Name your multiples: "))
print()
counter = 0
for i in range (1,11):
 ans = i*multiples
 print(i, "x", multiples, "=")
 inpu = int(input(">"))
 if inpu == ans:
   print("Correct!")
   counter+=1
 else:
   print("Incorrect! The correct answer should have been", ans)

 if counter == 10:
  print("You got 10 out of 10 correct!")
else:
  print("You got", counter, "out of 10 correct!")
  