'''Confronta due liste elemento per elemento
Hai due liste con numeri. Usa zip() per confrontare gli elementi nelle 
stesse posizioni e crea una nuova lista contenente la stringa 'uguali' 
se i numeri corrispondono, oppure 'diversi' se sono diversi.'''

lista1 = [5, 8, 10, 6]
lista2 = [5, 3, 10, 7]

nuova_lista = zip(lista1, lista2)

new_list = []
for a, b in nuova_lista:
    if a == b:
        new_list.append("uguali")
    else:
        new_list.append("diversi")
print(new_list)
