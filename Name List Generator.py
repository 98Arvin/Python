import os, time

names = []

def printNames():
  print()
  for name in names:
    print(name)
  print()

while True:
  print("Type reset to clear the list")
  time.sleep(1)
  os.system("clear")
  firstName = input("First Name: ").capitalize().strip()
  if firstName == "Reset":
    names = []
    os.system("clear")
    continue
  elif firstName == "View":
    printNames()
    time.sleep(2)
    os.system("clear")
    continue
  lastName = input("Last Name: ").capitalize().strip()
  name = str((firstName + " " + lastName))
  if name not in names:
    names.append(name)
  printNames()
  time.sleep(2)
  os.system("clear")
