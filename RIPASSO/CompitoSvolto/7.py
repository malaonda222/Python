'''Scrivere un programma che inizializzate due liste a e b della stessa lunghezza n, entrambe contenenti valori 
interi, calcoli la somma incrociata degli elementi.
Esempio:
a[1] + b[n-1], a[2] + b[n-2], ...
Memorizzare ogni somma incrociata in una nuova lista c e, quindi, visualizzare in output le liste a, b, c'''

lista_a: list = [1, 4, 6, 9, 20]
lista_b: list = [3, 5, 9, 33, 40]
lista_c = []

n: int = len(lista_a)
for i in range(n):
    lista_c.append(lista_a[i] + lista_b[n - i] - 1)

print(lista_c)