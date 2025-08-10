'''Genera una lista di numeri pari da 0 a 100 con list comprehension.'''

lista_numeri = [i for i in range(0, 101) if i % 2 == 0]
print(lista_numeri)

quadrati = [i**2 for i in range(0, 101) if i % 2 == 0]
print(quadrati)

divisibili_per = [i for i in range (1, 201) if i % 15 == 0]
print(divisibili_per)

