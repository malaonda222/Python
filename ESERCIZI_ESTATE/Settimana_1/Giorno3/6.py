'''Logica: Scrivi un algoritmo che verifichi se una lista è ordinata (crescente o decrescente).'''

def decrescente_crescente(lista: list):
    crescente = True 
    decrescente = True
    for i in range(len(lista) - 1):
        if lista[i] <= lista[i + 1]:
            decrescente = False
        else:
            crescente = False 

    if crescente:
        return "Crescente"
    elif decrescente:
        return "Decrescente"
    else:
        return "Non ordinata"

lista: list = [1, 2, 3, 4, 5]
lista2: list = [5, 4, 3, 2, 1]
print(decrescente_crescente(lista))
print(decrescente_crescente(lista2))

