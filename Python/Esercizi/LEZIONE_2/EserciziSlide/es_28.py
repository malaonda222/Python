menu:dict = {
    "pasta": 10.50, 
    "pizza": 9.00,
    "salad": 6.50,
    "wine": 4.00,
    "water": 2.30
}

pasta_price = menu["pasta"]
wine_price = menu["wine"]
print(f"Pasta: {pasta_price}\nVino: {wine_price}")

menu["dessert"] = 8.00
print(menu)

menu.pop("salad")
print(menu)

for value in menu.values():
    print(value)

for key in menu.keys():
    print(key)

for key, value in menu.items():
    print(key, value)
