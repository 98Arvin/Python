print("=== NAME GENERATOR ===")
print()
names = input("Type in your first name, last name, your mother's maiden name and the city you was born in: SEPARATE YOUR INPUTS WITH SPACEBAR:\n--> ").split()

firstName    = names[0].strip()
lastName     = names[1].strip()
maidenName   = names[2].strip()
city         = names[3].strip()
starWarsName = f"{firstName[0:3].title()}{lastName[0:2].lower()} {maidenName[0:2].title()}{city[-3:].lower()}"

print(f"Your nickname is {starWarsName}")
