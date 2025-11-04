'''Tema: Ordinamento di liste
Obiettivo: Ordinare manualmente una lista di numeri
Nome dell’esercizio: ordina_lista
Traccia:
Scrivi una funzione chiamata ordina_lista(lista_numeri) che riceve come parametro una lista di numeri interi o decimali non ordinata.
La funzione deve restituire una nuova lista contenente gli stessi numeri ordinati in ordine crescente (dal più piccolo al più grande).
Non puoi utilizzare funzioni o metodi built-in come sorted() o .sort().
Dovrai invece implementare un algoritmo di ordinamento manuale, come ad esempio Bubble Sort, Selection Sort o un approccio con confronti e scambi.
Se la lista è vuota, restituisci una lista vuota.'''

def ordina_lista(lista_numeri: list[int|float])-> list[int|float]:
    n = len(lista_numeri)
    for i in range(n):
        for j in range(0, n-1-i):
            if lista_numeri[j] > lista_numeri[j+1]:
                lista_numeri[j], lista_numeri[j+1] = lista_numeri[j+1], lista_numeri[j]
    return lista_numeri

print(ordina_lista([5, 2, 9, 1, 7]))


