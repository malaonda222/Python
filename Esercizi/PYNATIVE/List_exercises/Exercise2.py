'''Concatenare due elenchi in base all'indice'''

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

lista_completa = []
for i in range(len(list1)):
    lista_completa.append(list1[i] + list2[i])
print(lista_completa)


list3 = [1, 4, 5, 9]
list4 = [8, 9, 44444, 2]

lista_nuova = []
for i in range(len(list3)):
    lista_nuova.append(list3[i] + list4[i])
print(lista_nuova)