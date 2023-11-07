import os
import time

mylist = []

def printlist():
  os.system('clear')  
  print()
  for item in mylist:
    print(item)
  print()

while True:
  menu = input("To-Do-List Manager, Would you like to add, view, or remove your task: ")
  if menu == "view":
    printlist()
    time.sleep(1)
  elif menu == "add":
    item = input("What would you like to add: ")
    mylist.append(item)
  elif menu == "remove":
    item = input("What do you want to remove? :")
    if item in mylist:
     mylist.remove(item)