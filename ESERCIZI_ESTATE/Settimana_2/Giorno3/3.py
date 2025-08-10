'''Mappa ogni numero in una lista al suo cubo.'''

numeri: list = [1, 5, 4, 6, 2, 222, 7, 9]
cubi = list(map(lambda numero: numero**3, numeri))
print(cubi)

def cubo(x):
    return x**3
cubi2 = list(map(cubo, numeri))
print(cubi2)