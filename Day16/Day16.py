print("Fill in the blank lyrics!")
print("(Type in the blank lyrics and see if you are as cool as me).")
print()
counter = 1
while True:
 answer = input("Never going to ______ you up.")
 if answer == "give" or answer == "Give":
  counter += 1
  break
 
 else:
  print("Try again.")
print("Well done! You have got it right", counter,"attempts!" )
      
     