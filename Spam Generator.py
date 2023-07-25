import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear")
  print("List Of Emails")
  print()
  for index in range(len(listOfEmail)):
    print(f"{index + 1}: {listOfEmail[index]}")
  time.sleep(3)

randomText = ["Spam is not good, spam is not niceSpam is not good, spam is not niceSpam is not good, spam is not nice", "GET SPAMMEDGET SPAMMEDGET SPAMMEDGET SPAMMEDGET SPAMMEDGET SPAMMEDGET SPAMMEDGET SPAMMED", "You are getting spammed!!!!You are getting spammed!!!!You are getting spammed!!!!", "i love spam", "no i dont love spam", "spam is not cool", "spam rhymes with ham"]


def startSpam():
  os.system("clear")
  for email in range(len(listOfEmail)):
    randomTextLength = (len(randomText))
    if email < randomTextLength:
      print(listOfEmail[email])
      print(randomText[email])
    else:
      break
    email += 1
    time.sleep(2)
    os.system("clear")

while True:
  print("SPAMMER")
  menu = input("1: Add email \n2: Remove email\n3: Show emails\n4: Get SPAMMING\n5: Quit program\n--> ")
  if menu == "1":
    email = input("Email: ")
    listOfEmail.append(email)
  elif menu == "2":
    email = input("Email: ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    print(prettyPrint())
  elif menu == "4":
    print (startSpam())
  elif menu == "5":
    exit()
    
  time.sleep(0.1)
  os.system("clear")

