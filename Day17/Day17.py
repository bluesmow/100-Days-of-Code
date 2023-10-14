print("E P I C 🪨 📄 ✂️  B A T T L E")
print()
print("Select your move (R, P or S) ")
print()
player1score = 0
player2score = 0
while True:
  player1 = input("Player 1 >")
  player2 = input("Player 2 >")
  print()
  
  if player1 == "R" and player2 == "R":
    print("It's a tie!")
  elif player1 == "R" and player2 == "P":
     print("Player 2 Wins!")
     player2score += 1
  elif player1 == "R" and player2 == "S":
     print("Player 1 Wins!")
     player1score += 1
  elif player1 == "P" and player2 == "R":
     print("Player 1 Wins!")
     player1score += 1
  elif player1 == "P" and player2 == "P":
     print("It's a tie!")
  elif player1 == "P" and player2 == "S":
     print("Player 2 Wins!")
     player2score +=1
  elif player1 == "S" and player2 == "R":
     print("Player 2 Wins!")
     player2score +=1
  elif player1 == "S" and player2 == "P":
     print("Player1 Wins!")
     player1score +=1
  elif player1 == "S" and player2 == "S":
     print("It's a tie!")
  else:
    print("Invalid move!")
  print("Player1 has", player1score, "points")
  print("Player2 has", player2score,"points")
  if player1score == 3 or player2score == 3:
    print("Thanks for playing!")
    exit()

  else:
   continue

