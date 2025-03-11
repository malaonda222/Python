# Esercizio 7
'''Scrivere un programma che inizializzate due liste a e b della stessa lunghezza n, entrambe contenenti valori 
interi, calcoli la somma incrociata degli elementi.
Esempio:
a[1] + b[n-1], a[2] + b[n-2], ...
Memorizzare ogni somma incrociata in una nuova lista c e, quindi, visualizzare in output le liste a, b, c'''

# inizializzare la lunghezza delle liste a e b
n = 3 
lista_a = []
for x in range(n):
    numero = float(input("Inserisci un numero intero alla lista a: ")) # chiedere all'utente di inserire valori interi per la lista a
    if numero.is_integer(): # verificare se il numero inserito è intero
        lista_a.append(numero)
        print(f"Lista a: {lista_a}") # stampa lista a
    else:
        print("Errore.")

lista_b = []
for x in range(n):
    numero = float(input("Inserisci un numero intero ala lista b: ")) # chiedere all'utente di inserire valori interi per la lista b
    if numero.is_integer(): # verificare se il numero inserito è intero
        lista_b.append(numero)
        print(f"Lista b: {lista_b}") # stampa lista b
    else:
        print("Errore.")

# creazione della lista c
lista_c = [] 
for x in range(n): 
    somma = lista_a[x] + lista_b[(n-x) -1]
    lista_c.append(somma)

# stampa dei risultati
print(lista_a)
print(lista_b)
print(lista_c)
