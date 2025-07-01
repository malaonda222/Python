# Identificare la grandezza di una lista
lista = []

# ciclo While
while True:
    elemento = input("Inserisci un elemento, inserisci stop per uscire: ")
    
    if elemento == "stop":
        break
    
    lista.append(elemento)

# match statement
match len(lista):
    case 0:
        print("La lista è vuota.")
    case 1:
        print("Lista con un elemento.")
    case _:
        print(f"Lista è lunga {len(lista)} elementi.")
