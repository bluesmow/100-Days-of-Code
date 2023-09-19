print("Generation Identifier")
print()

birthYear = int(input("What year were you born?"))
if birthYear >= 1883 and birthYear <=1900:
  print("You are a Lost Generation.")
elif birthYear >= 1901 and birthYear <= 1927:
  print("Hey, Greatest Generation! ")
elif birthYear >= 1928 and birthYear <= 1945:
  print("Silent Generation! What's up?")
elif birthYear >= 1946 and birthYear <= 1964:
  print("Baby Boomers!How you doing?")
elif birthYear >= 1965 and birthYear <= 1980:
  print("Generation X")
elif birthYear >= 1981 and birthYear <= 1996:
  print("Hah! Millenial! Avocado toast and Starbucks much!") 
elif birthYear >= 1997 and birthYear <= 2012:
  print("Generation Z of IPAD kids ")
elif birthYear >= 2013:
  print("Hey, Gen Alpha!")
else: 
  print("Try again!")