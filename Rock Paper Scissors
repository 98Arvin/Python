from getpass import getpass as input

print("********* E P I C 🪨 📃✂️  B A T T L E *********")
print()

score1 = 0
score2 = 0

while True:
    player1 = input("PLAYERO UNO: Select your move (R, P, S): ")
    player2 = input("PLAYERO DOS: Select your move (R, P, S): ")
    #DRAW SCENARIOS
    if player1 == "R" and player2 == "R" or player1 == "P" and player2 == "P" or player1 == "S" and player2 == "S":
        print()
        print("******* PLAYERO UNO WINS *******")

#PLAYER 1 WIN SCENARIOS
    elif player1 == "R" and player2 == "S" or player1 == "S" and player2 == "P" or player1 == "P" and player2 == "R":
        print()
        print("******* PLAYERO UNO WINS *******")
        score1 += 1

#PLAYER 2 WIN SCENARIOS
    elif player2 == "R" and player1 == "S" or player2 == "S" and player1 == "P" or player2 == "P" and player1 == "R":
        print()
        print("******* PLAYERO DOS WINS *******")
        score2 += 1

#CHEAT
    elif player1 == "W":
        print()
        print("******* PLAYERO UNO WINS *******")
        score1 += 1
    elif player2 == "W":
        print()
        print("******* PLAYERO DOS WINS *******")
        score2 += 1

    if score1 == 3:
        print()
        print()
        print("✨✨✨✨ PLAYERO UNO WINS THE WHOLE GAME ✨✨✨✨")
        print()
        print()
        print("  ✨✨✨✨  PLAYERO UNO score  |  ", score1, " ✨✨✨✨")
        print("  ✨✨✨✨  PLAYERO DOS score  |  ", score2, " ✨✨✨✨")
        print()
        print()
        exit()
    if score2 == 3:
        print()
        print()
        print("✨✨✨✨ PLAYERO DOS WINS THE WHOLE GAME ✨✨✨✨")
        print()
        print()
        print("  ✨✨✨✨  PLAYERO UNO score  |  ", score1, " ✨✨✨✨")
        print("  ✨✨✨✨  PLAYERO DOS score  |  ", score2, " ✨✨✨✨")
        print()
        print()
        exit()

#ERROR SCENARIO
    else:
        continue
