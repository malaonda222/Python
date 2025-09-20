'''Esercizio 3 - Minimo e massimo
Tema: Analisi di lista
Obiettivo: Trovare gli estremi
Traccia:
Scrivi una funzione che ritorni il valore minimo e massimo in una lista di numeri senza usare le funzioni min() e max().'''

def minimo_massimo(lista_numeri: list[int]) -> tuple:
    if not lista_numeri:
        return None, None 
    minimo = lista_numeri[0]
    massimo = lista_numeri[0]
    for element in lista_numeri:
        if element < minimo:
            minimo = element 
        if element > massimo:
            massimo = element 
    return minimo, massimo 

def minimo_massimo1(lista_numeri: list[int]) -> tuple:
    minimo = min(numero for numero in lista_numeri)
    massimo = max(numero for numero in lista_numeri)
    return minimo, massimo


lista_numeri = [1, 3, 4, 10, 111, 2, 56, 2]
print(minimo_massimo(lista_numeri))
print(minimo_massimo1(lista_numeri))
