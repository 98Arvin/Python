player1 = input("→ What's your name Player one?: ")
player2 = input("→ What's your name Player two?: ")
print()
print()
print("🎲🎲🎲🎲 S T A R T  G A M E 🎲🎲🎲🎲")
print()
print()


counter = 0
score1 = 0
score2 = 0

while True:
  import random
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  if dice1 > dice2:
    print(player1, "rolled...  ", dice1, "  and  ", player2, "rolled...  ", dice2, "  so,", player1, "wins 🥳🥳🥳")
    print()
    counter += 1
    score1 += 1
  elif dice2 > dice1:
    print(player1, "rolled...  ", dice1, "  and  ", player2, "rolled...  ", dice2, "  so,", player2, "wins 🥳🥳🥳")
    print()
    counter += 1
    score2 += 1
  
  elif dice1 == dice2:
    print("DRAW")

  if counter == 10:
    print(player1,"SCORE:", score1, player2,"SCORE:", score2)
    if score1 > score2:
      print(player1, "WINS THE GAME")
    elif score2 > score1:
      print(player2, "WINS THE GAME")
    else:
      print("IT'S A DRAW!!")
    break
