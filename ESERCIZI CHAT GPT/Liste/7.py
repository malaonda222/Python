'''Esercizio 7 - Liste annidate
Tema: Liste di liste
Obiettivo: Sommare elementi annidati
Traccia:
Scrivi una funzione che, data una lista di liste di numeri, ritorni la somma totale di tutti i numeri.'''

def somma_elementi(lista_numeri: list[list[int]]) -> int:
    somma = 0
    for lista in lista_numeri:
        somma_parziale = 0
        for element in lista:
            somma_parziale += element 
        somma += somma_parziale
    return somma

def somma_elementi1(lista_numeri: list[list[int]]) -> int:
    return sum(sum(lista) for lista in lista_numeri)

lista_numeri = [[1, 2, 3], [4, 5], [6, 7]]
print(somma_elementi(lista_numeri))
print(somma_elementi1(lista_numeri))
