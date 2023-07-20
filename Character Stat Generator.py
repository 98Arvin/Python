print("⚔️ CHARACTER STAT GENERATOR ⚔️")

def rollDice(sides):
  import random
  dice = random.randint(1,sides)
  return dice
def charHealth():
  while True:
    health = rollDice(6) * rollDice(8)
    if health > 20:
      return health
      break
    else:
      continue

health1 = charHealth()
health2 = charHealth()
health3 = charHealth()

player1 = input("Name your warrior: ")
print("Your warrior", player1, "has", health1, "HP")
player2 = input("Name your warrior: ")
print("Your warrior", player2, "has", health2, "HP")
player3 = input("Name your warrior: ")
print("Your warrior", player3, "has", health3, "HP")
