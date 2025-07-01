'''Concatenare due elenchi nel seguente ordine'''

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

lista_finale = []
for x in list1:
   for y in list2:
    lista_finale.append(x + y)
print(lista_finale)

result = [x + y for x in list1 for y in list2]
print(result)
    