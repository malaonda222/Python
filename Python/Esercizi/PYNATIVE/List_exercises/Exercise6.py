'''Rimuovere le stringhe vuote dall'elenco delle stringhe'''

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
lista_senza_vuoti = []

for item in list1:
    if item != "":
        lista_senza_vuoti.append(item)
print(lista_senza_vuoti)

result = list(filter(None, list1))
print(result)