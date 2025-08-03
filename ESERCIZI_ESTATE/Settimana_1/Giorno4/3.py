'''Aggiungi un elemento a una tupla (tip: crea una nuova).'''

tupla1: tuple = ("d", 1, 2, 10, 22, "c")
lista1: list = list(tupla1)
lista1.append("b")
tupla2: tuple = tuple(lista1) 
print(tupla2)