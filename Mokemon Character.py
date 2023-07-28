import os, time

#game title
print("=== MOKEMON CHARACTER ===")
time.sleep(2)
os.system("clear")

#add value to your mokemon
mokemon = {"name": None, "species": None, "type": None, "special move": None, "hp": None, "mp": None}
counter = 0

for i in mokemon.keys():
  counter += 1
  if counter == 3:
    print("Choose Fire, Water, Earth or Air ⚔️")
  mokemon[i] = input(f"Type in {i.title()}: ")
  os.system("clear")

#change color based on type
typeColor = mokemon["type"][0].lower()

if typeColor == "e":
  print("\033[32m", end="")
elif typeColor== "a":
  print("\033[37m", end="")
elif typeColor == "f":
  print("\033[31m", end="")
elif typeColor == "w":
  print("\033[34m", end="")
else:
  print("\033[33m", end="")

#print out the mokemon
for i, j in mokemon.items():
  print(f"{i.title()}: {j.title()}")
