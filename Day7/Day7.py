print(" 🕵️‍♂️ Fake Fan Finder 👀 ")
print("--------------------------------")
anime = input("What's your favorite Anime?:")
if anime == "One Piece":
  character = input("Oh really?! Name me any of the characters? ")
  if character == "Nami":
      job = input("You got that by pure chance.Okay then , what is her job on the ship?")
    
      if job =="Navigator":
        bounty = input("Hmph! What was her first bounty then?")
        if bounty == "Marines":
          print("Well you are a true one Piece Fan")
        else: 
          print("See! FAKE One Piece Fan")  
      else:
        print("See!Fake One Piece Fan!")
  else:
      print("See! FAKE One piece fan!")     
elif anime == "Jujustu Kaisen":
  print("Lemme guess, You are Gojo Simp!")
else:
  print("That sucks :(")