'''Scrivere un programma che inizializzate due liste a e b della stessa lunghezza n, entrambe contenenti valori 
interi, calcoli la somma incrociata degli elementi.
Esempio:
a[1] + b[n-1], a[2] + b[n-2], ...
Memorizzare ogni somma incrociata in una nuova lista c e, quindi, visualizzare in output le liste a, b, c'''

n = 4
count_a = 1
count_b = 1
lista_a = []
for numero in range(n):
    numero = input(f"Inserisci {count_a}° numero per la lista a: ")
    if numero.lstrip('-').isdigit():
            numero = int(numero)
            lista_a.append(numero)
            count_a += 1
    else:
        print("Inserisci un numero intero.")

lista_b = []
for numero in range(n):
    numero = input(f"Inserisci {count_b}° numero per la lista b: ")
    if numero.lstrip('-').isdigit():
            numero = int(numero)
            lista_b.append(numero)
            count_b += 1
    else:
        print("Inserisci un numero intero.")

lista_c = []
somma_incrociata = 0
for x in range(n):
    somma_incrociata = lista_a[x] + lista_b[(n-x) -1]
    lista_c.append(somma_incrociata)


print(f"Lista a: {lista_a}.")
print(f"Lista b: {lista_b}.")
print(f"La somma incrociata degli elementi delle due liste è: {lista_c}.")

