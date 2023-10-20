print("Replit Login System")
print()
def login():
  while True:
    username = input("What is your username?:  ")
    password = input("What is your password?:  ")
    if username == "Minnu" or username == "minnu" and \
    password == "Minnu123" or password =="minnu123" : 
      print("Welcome, Minnu!")
      break
    else:
      print("Incorrect username or password" )
      print()
login()