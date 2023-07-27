name = input("What's your name?: ").strip().capitalize()
birth = input("When were you born?: ").strip()
number = input("What's your number?: ").strip()
email = input("What's your email?: ").strip()
address = input("What's your Address?: ")
creditCard0 = {"name":name, "birth":birth, "number":email, "email":email, "address":address}

name = input("What's your name?: ").strip().capitalize()
birth = input("When were you born?: ").strip()
number = input("What's your number?: ").strip()
email = input("What's your email?: ").strip()
address = input("What's your Address?: ")
creditCard1 = {"name":name, "birth":birth, "number":email, "email":email, "address":address}

print(f'''
CARD ONE:
Name:     {creditCard0["name"]}
Birth:    {creditCard0["birth"]}
Number:   {creditCard0["number"]}
Email:    {creditCard0["email"]}
Address:  {creditCard0["address"]}''')

print(f'''
CARD TWO:
Name:     {creditCard1["name"]}
Birth:    {creditCard1["birth"]}
Number:   {creditCard1["number"]}
Email:    {creditCard1["email"]}
Address:  {creditCard1["address"]}''')
