import random, os, time

print("=== HANGMAN ===")
time.sleep(1.5)
print("Are you ready?")
time.sleep(1.5)
print("Let's begin!")
time.sleep(2)
os.system("clear")

def game():
  #game rules and definitions
  listOfWords = ["british", "norway", "hairless", "orange", "unfortunately", "stranded", "witcher", "wisdom", "relentless", "worldwide", "nurmagomedov", "challenge", "hangman", " "]
  secret = (random.choice(listOfWords))
  picked = []
  lives = 6
  #game starts here
  while True:
    #asks user for a letter and adds it "Pickedif not already picked or it's not a spacebar or just empty
    user = input("Type a letter: ").lower()
    if user == "":
      os.system("clear")
      continue
    user = user[0].lower()
    if user == " ":
      os.system("clear")
      continue
    os.system("clear")
    if user in picked:
      print("Already picked")
      continue
    picked.append(user)

    #if users letter input already in the secret word, print something, if not, deduct from lives left
    if user in secret:
      print("You found one")
    else:
      print("Nope! Incorrect letter.")
      lives -= 1

    #print every letter in the secret word, if user correct. Else just add "_" instead and keep "allLetters" to False so game does not finish
    allLetters = True
    print()
    for i in secret:
      if i in picked:
        print(i, end="")
      else:
        print("_", end="")
        allLetters = False

    #if allLetters is true then game can finish with a message and break loop
    if allLetters:
      os.system("clear")
      print(f" is correct. YOU WIN! You had {lives} lives left!")
      break
    #if lives 0, give lost message and break loop (end game), else print remaining lives and continue
    if lives <= 0:
      print(": 0 lives left. You lose!")
      break
    else:
      print(f": {lives} left")
        

while True:
  game()
  time.sleep(3)
  os.system("clear")
  again = input("Wanna play again? YES or NO: ")
  if again[0].lower() == "y":
    continue
  else:
    exit()
