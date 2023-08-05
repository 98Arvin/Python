import random, os, time

play = input("Press enter to play!\n")
counter = 0
time.sleep(0.5)

def card():
  print(f'''
  {bingo[0][0]} |  {bingo[0][1]}   | {bingo[0][2]}
  -------------
  {bingo[1][0]} | {bingo[1][1]} | {bingo[1][2]}
  -------------
  {bingo[2][0]} |  {bingo[2][1]}   | {bingo[2][2]}\n''')


if play == "" or play != "":
  def randomInt():
    number = random.randint(10,90)
    return number
    
  bingo = [ [randomInt(), randomInt(), randomInt()],
            [randomInt(), "BINGO",     randomInt()],
            [randomInt(), randomInt(), randomInt()] ]
  
  card()

  time.sleep(2)
  
while True:  
  guess = int(input("Next Number: "))
  for row in range(len(bingo)):
    for item in range(len(bingo)):
      if guess == bingo[row][item]:
        print("NICE")
        bingo[row][item] = "X"
        counter += 1
        os.system("clear")
        card()
  if counter == 8:
    os.system("clear")
    print("THE GAME IS OVER")
    break
