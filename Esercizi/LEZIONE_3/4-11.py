# My Pizzas, Your Pizzas
favorite_pizzas = ["Margherita", "Salamino", "Calabrese"]

friend_pizzas = ["Margherita", "Salamino", "Calabrese"]

favorite_pizzas.append("Capricciosa")
print(f"My favorite pizzas are: ", favorite_pizzas)
for item in favorite_pizzas:
    print(f"My favorite pizzas is: {item}")

friend_pizzas.append("Quattro Stagioni")
print(f"My friend's favorite pizzas are", friend_pizzas)
for item in friend_pizzas:
    print(f"My friend's favorite pizzas is: {item}")