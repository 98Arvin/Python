import os, time

toDoList = []

def printList():
  print("------")
  for i in toDoList:
    print(i)
  print("------")

while True:
  decision = input("Do you want to view, add or edit the todo list?: ")
  if decision == "view":
    os.system("clear")
    printList()
    time.sleep(2)
  elif decision == "add":
    os.system("clear")
    item = input("Type in item: ")
    toDoList.append(item)
  elif decision == "edit":
    os.system("clear")
    printList()
    print()
    remove = input("What have you completed or want removed?: ")
    toDoList.remove(remove)
    os.system("clear")
  else:
    os.system("clear")
    print(f"try again 😊")
    time.sleep(1)
    os.system("clear")
    
    
