print("*** EASIEST MATH GAME ***")
print()
name = input("What's your name? ")
print("Hello", name, "today we're doing math! 😒")
print()

multiply = int(input("What is your favorite number from 2 to 10?: "))
score = 0

for i in range (1,11):
  if multiply > 2 and multiply < 10:
    correctAnswer = i*multiply
    print("Question:", i, "X", multiply)
    answer = int(input("Answer: "))
    if answer == correctAnswer:
      score += 1
      print("Correct!")
      print()
    else:
      print("Wrong!")
      print()
  else:
    print("Try again")
    exit()

if score == 10:
  print("Damn, you got them all right!")
else:
  print("You got", score, "out of 10 correct.")
    

