min = int(input("How many seconds are there in a minute:"))
hrs = int(input("How many minutes are there in an hour:"))
day = int(input("How many hours are there in a day:"))
year = int(input("How many days in a year:"))
daysinyear = 365
daysinleapyear = 366
answer = min*hrs*day*daysinyear
leapanswer = min*hrs*day*daysinleapyear

if year == 366:
  print("It's a leap year:", leapanswer)
else:
  print("Number of seconds in a year will be",answer)
  
