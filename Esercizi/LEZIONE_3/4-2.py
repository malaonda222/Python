# Animals

list_animals:list = ["dog", "cow", "horse"]

print(f"The {list_animals[0]} is a beautiful animal")
print(f"The {list_animals[1]} is a big animal")
print(f"The {list_animals[2]} is a riding animal")

# opzione con ciclo for
for item in list_animals:
    print(item)
    print(f"The {item} would make a great pet")

# # opzione con ciclo while
lista_animali = []
i = 1

while i <= 5:
    animale = input("Inserire il nome di un animale: ")
    lista_animali.append(animale)
    i = i + 1
    print(lista_animali)

print(f"Gli animali scelti sono: {lista_animali}")

# opzione con ciclo while (True)
lista_animali_1 = []

while True:
    animal = input("Inserire il nome di un animale (inserisci stop per terminare il ciclo): ")
    if animal == "stop":
        break
    lista_animali_1.append(animal)
    print(f"Hai scelto l'animale: {animal}")
print(lista_animali_1)