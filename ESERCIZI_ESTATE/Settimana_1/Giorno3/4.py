'''Crea una lista di quadrati dei primi 10 numeri.'''

lista_numeri = []
for i in range(10):
    lista_numeri.append(i**2)
print(lista_numeri)

print(list([i**2 for i in range(10)]))