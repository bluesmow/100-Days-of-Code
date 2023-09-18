print("MY LOGIN SYSTEM")
print("++++++++++++++++")
username = input("Username >")
password = input("Password >")
print()
if username == "David"  and password == "totallyNotBald" :
  print("""Why hello there David, what a lovely accent you have, 
  you could have charmed your way in here without
  a password.
  
  Have a great day. 
  
  Don't forget to wear a hat in the sun!""")
elif username == "Cassandra" and password == "NotCassandra":
   print("Hi Cassandra")
else:
  print("Go Away!")