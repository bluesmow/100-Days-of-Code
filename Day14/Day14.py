print("E P I C 🪨 📄 ✂️  B A T T L E")
print()
print("Select your move (R, P or S) ")
print()
player1 = input("Player 1 >")
player2 = input("Player 2 >")
print()
print("Player 1 chose:", player1)
print("Player 2 chose:", player2)
print()
if player1 == "R" and player2 == "R":
  print("It's a tie!")
elif player1 == "R" and player2 == "P":
   print("Player 2 Wins!")
elif player1 == "R" and player2 == "S":
   print("Player 1 Wins!")
elif player1 == "P" and player2 == "R":
   print("Player 1 Wins!")
elif player1 == "P" and player2 == "P":
   print("It's a tie!")
elif player1 == "P" and player2 == "S":
   print("Player 2 Wins!")
elif player1 == "S" and player2 == "R":
   print("Player 2 Wins!")
elif player1 == "S" and player2 == "P":
   print("Player1 Wins!")
elif player1 == "S" and player2 == "S":
   print("It's a tie!")
else:
  print("Invalid move!")
      