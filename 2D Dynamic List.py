funList = []

def prettyPrint():
  print()
  for row in funList:
    for things in row:
      print(f"{things:^10}", end=" | ")
    print()
  print()

while True:
  name = input("What is your name? ").capitalize()
  age = input("What is your age? ")
  pref = input("Mac or PC? ").capitalize()
  row =  [name, age, pref]
  funList.append(row)
  exit = input("Do you want to exit? Y/N: ")
  if exit.strip().lower()[0] == "y":
    break
  

prettyPrint()
