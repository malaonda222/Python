'''Scrivi una funzione chiamata filtra_e_somma che prende in input:
una lista di liste di numeri interi lista_numeri
un intero soglia
La funzione deve:
Per ogni sottolista in lista_numeri, selezionare solo i numeri minori o uguali alla soglia.
Calcolare la somma dei numeri filtrati in ogni sottolista.
Restituire una nuova lista contenente le somme (una per ogni sottolista).'''

def filtra_e_somma(lista_numeri: list[list[int]], soglia: int) -> list[int]:
    somme = []
    for sottolista in lista_numeri:
        numeri_somma = 0
        for numero in sottolista:
            if numero <= soglia:
                numeri_somma += numero 
        somme.append(numeri_somma)
    return somme 


def filtra_e_somma1(lista_numeri: list[list[int]], soglia: int) -> list[int]:
    return [sum(numero for numero in sotto_lista if numero <= soglia) for sotto_lista in lista_numeri]


lista = [[1, 10, 3], [5, 12, 7], [20, 0, 4]]
soglia = 7

print(filtra_e_somma(lista, soglia))
print(filtra_e_somma1(lista, soglia))
