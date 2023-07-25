import time, os
todoList = []

def printList():
  for item in todoList:
    print(item)

def pauses():
  print("Not in the list")
  print(".")
  time.sleep(1)
  print(".")
  time.sleep(1)
  print(".")
  time.sleep(1)


while True:
  os.system("clear")
  menu = input("1: Add\n2: Remove\n3: Change\n4: Show\n--> ")
  if menu == "1":
    item = input("What to add?: ")
    todoList.append(item)
    time.sleep(1)
  elif menu == "2":
    printList()
    print()
    item = input("What to remove?: ")
    check = input("Are you sure?: ")
    if check[0] == "y":
      if item in todoList:
        todoList.remove(item)
      else:
        pauses()
  elif menu == "3":
    printList()
    print()
    item = input("What to change?: ")
    new = input("What to change it to?: ")
    for i in range(0,len(todoList)):
      if todoList[i] == item:
        todoList[i] == new
  elif menu == "4":
    print()
    print("THE LIST")
    printList()
    time.sleep(4)
