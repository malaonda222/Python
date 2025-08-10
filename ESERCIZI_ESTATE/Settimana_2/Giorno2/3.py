'''Crea una lista di numeri quadrati divisibili per 3.'''

quadrati = [i**2 for i in range(1, 31) if (i**2) % 3 == 0]
print(quadrati)