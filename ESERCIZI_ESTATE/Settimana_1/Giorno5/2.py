'''Stampa solo i numeri divisibili per 3 e 5.'''

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
