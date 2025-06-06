'''3) Scrivere in Python dei cicli che stampino le seguenti sequenze 
di valori:
a) 2, 4, 6, 8, 10, 12, 14
b) 1, 4, 7, 10, 13
c) 30, 25, 20, 15, 10, 5, 0
d) 5, 15, 25, 35, 45'''



cont = 2
lista_1 = []
while cont <= 14:
    lista_1.append(cont)
    cont += 2
print(*lista_1)


lista_2 = []
for i in range(1, 14, 3):
    lista_2.append(i)
print(*lista_2)


lista_3 = []
for i in range(30, -1, -5):
    lista_3.append(i)
print(*lista_3)


lista_4 = []
cont1 = 5
while cont1 <= 45:
    lista_4.append(cont1)
    cont1 += 10
print(*lista_4)
