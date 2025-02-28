#opzione ciclo for

# Pizzas
favorite_pizza = ["Margherita", "Salamino", "Calabrese"]

for item in favorite_pizza:
    # print(item)
    print(f"I like {item} pizza")
    print(f"I adore pizza!")


# opzione con il ciclo while
favorite_pizza_1 = []
i = 1
while i <= 3:
    pizza = (input("Inserisci il nome di una pizza: "))
    favorite_pizza_1.append(pizza)
    i = i + 1
    print(favorite_pizza_1)


