print("Tip Calculator")
print()
bill = float(input("How much did you spend?"))
print()
percentage = int(input("What percentage do you want to tip?"))
print()
people = int(input("How many people in you your group?"))
print()
billwithpercentage = percentage / 100 * bill + bill
billperperson = billwithpercentage/people 

answer = round(billperperson , 2)
print("You all owe", answer )