# Identificare la grandezza di una lista
n = input("Inserisci niente, una parola o più parole: ")

lista = []
lista.append(n)

match lista:
    case []:
        print("La lista è vuota.")
    case [elemento]:
        print("Lista con un elemento.")
    case [*elementi]:
        print("Lista lunga.")