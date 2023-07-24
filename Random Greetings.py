import random
greets = ["dude", "man", "potato", "cool guy", "bad boy"]
randomGreet = greets[random.randint(0,4)]
name = input(f"Hey {randomGreet}. What's your name?\n\n--> ")
greeting = ["Hei!", "Hello!", "Guten Tag!", "Hola!", "Salam!", "Privet", "Nin hao!", "Konnichiwa!", "Oi!", "Namaste!", "Hai!", "Ciao!", "God Dag!", "Bonjou!", "Xin chao!", "Merhaba!", "Szia!", "Kamusta!", "Barev!", "Ahoj!"]
number = random.randint(0,19)
print(f"{greeting[number]} {name} 😊")
