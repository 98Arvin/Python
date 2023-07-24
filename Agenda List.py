import os, time

myAgenda = []

def list():
  print()
  for i in myAgenda:
    print(i)
  print()

while True:
  item = input("What's next on the Agenda?: ")
  myAgenda.append(item)
  list()
  quit = input("Press ENTER to continue or type NO to exit: ")
  if quit == "":
    os.system("clear")
    print("OK!")
    time.sleep(1)
    os.system("clear")
    
    continue
  else:
    break
