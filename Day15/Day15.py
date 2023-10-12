print("AMAZON ALEXA MODEL")
print("__________")
animal = ""
exit = "no"
while exit == "no":
  animal = input("Which animal do you want? :")
  if animal == "Cow" or animal == "cow":
    print("A Cow goes moo")
  elif animal == "Lemur" or animal == "lemur":
    print("Umm.. the Lesser Syrian Lemur goes snort")
  elif animal == "Sheep" or animal == "sheep":
    print("A Sheep goes baaaaaa")
  elif animal == "Hamster" or animal == "hamster":
    print("Hamster goess crucnchhh")
  elif animal == "Pig" or animal == "pig":
    print("Oiinkkkk!")
  elif animal == "Dog" or animal == "dog":
    print("Bark bark goes Hailey's Dog")
  elif animal == "Cat" or animal == "cat":
    print("Meow meow the  Cat")
  elif animal == "Duck" or animal == "duck":
    print("Quack quackkkkkk")
  else:
    print("I don't know that animal")
    
  exit = input("Do you want to exit?")