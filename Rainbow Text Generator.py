import os, time
print("\033[33m","===", "\033[0m", "rainbow text generator".upper(), "\033[33m", "===", "\033[0m", "")
print()
startProgram = input("Do you want to start the rainbow text generator? You should..it's good for your health :) YES or NO: ")

def rainbowText():
  text = input("Type something: ")
  chars = ["a", "r", "v", "i", "n", "d", "o", "e", "s", "t", "c", "f", "g", "h", "j", "k", "l", "m", "n", "p"]
  counter = 1
  
  for letter in text:
    if letter.lower() in chars:
      print(f"\033[3{counter}m", end="")
      if counter > 6:
        counter = 1
      else:
        counter += 1
    print(letter, end="")
    print("\033[0m", end="")
  
if startProgram[0].lower() == "y":
  time.sleep(1)
  os.system("clear")
  rainbowText()
else:
  print("You are boring...")
  time.sleep(2)
  exit()
