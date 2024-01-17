import os
import time

def load_todo():
    try:
        with open("to.do", "r") as f:
            return eval(f.read())
    except FileNotFoundError:
        return []

def save_todo(todo):
    with open("to.do", "w") as f:
        f.write(str(todo))

def add():
    time.sleep(1)
    os.system("clear")
    name = input("Name > ")
    date = input("Due Date (YYYY-MM-DD) > ")
    priority = input("Priority > ").capitalize()
    row = [name, date, priority]
    todo.append(row)
    print("Added")

def view():
    time.sleep(1)
    os.system("clear")
    options = input("1: All\n2: By Priority\n> ")
    if options == "1":
        for row in todo:
            print(" | ".join(map(str, row)))
        print()
    else:
        priority = input("What priority? > ").capitalize()
        for row in todo:
            if priority in row:
                print(" | ".join(map(str, row)))
        print()
    time.sleep(1)

def edit():
    time.sleep(1)
    os.system("clear")
    find = input("Name of todo to edit > ")
    found = False
    for row in todo:
        if find in row:
            found = True
    if not found:
        print("Couldn't find that")
        return
    todo[:] = [row for row in todo if find not in row]
    name = input("Name > ")
    date = input("Due Date (YYYY-MM-DD) > ")
    priority = input("Priority > ").capitalize()
    row = [name, date, priority]
    todo.append(row)
    print("Edited")

def remove():
    time.sleep(1)
    os.system("clear")
    find = input("Name of todo to remove > ")
    todo[:] = [row for row in todo if find not in row]

todo = load_todo()

while True:
    menu = input("1: Add\n2: View\n3: Edit\n4: Remove\n> ")
    if menu == "1":
        add()
    elif menu == "2":
        view()
    elif menu == "3":
        edit()
    elif menu == "4":
        remove()

    time.sleep(1)
    os.system("clear")
    save_todo(todo)
