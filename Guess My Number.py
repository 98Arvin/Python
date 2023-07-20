import random

print("GUESS MY NUMBER")
number = random.randint(1, 1000000)
counter = 1

while True:
  guess = int(input("What is your guess?: "))
  if guess < 0:
    print("Exiting game..")
    print()
    exit()
  if guess == number:
    print("CORRECT!")
    break
  elif guess < number:
    print("TOO LOW")
    counter += 1
    continue
  elif guess > number:
    print("TOO HIGH")
    counter += 1
    continue

print("It took you", counter, "guesses.")
