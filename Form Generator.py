import os, time

print("=== FORM GENERATOR ===")
time.sleep(2)
os.system("clear")
website = {}

while True:
  newValue = input("What do you want to add?: ")
  if newValue == "" or newValue == " ":
    os.system("clear")
    continue
  website[newValue] = [None]
  exit = input("Do you want to exit and start the generator? YES or NO: ")
  if exit == "" or exit == " ":
    os.system("clear")
    continue
  elif exit[0].lower() == "y":
    os.system("clear")
    break
  else:
    os.system("clear")
    continue

for key in website.keys():
  website[key] = input(f"{key}: ") #Changes the value inside 

print()
for tag, value in website.items():
  print(f"{tag}: {value}")
