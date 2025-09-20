'''
Esercizio 5
Tema: Liste annidate e trasformazioni
Obiettivo: Allenarsi a filtrare e trasformare elementi in liste di liste
Nome dell’esercizio: Doppio filtro e moltiplicazione
Traccia:
Hai una lista di liste di numeri, ad esempio:

Scrivi una funzione filtra_e_moltiplica(liste, n) che:
    1. Filtri solo i numeri maggiori di n in ogni sotto-lista.
    2. Moltiplichi per 2 ogni numero filtrato.
'''
def filtra_e_moltiplica(lista_numeri: list[list[int]], soglia: int) -> list[list[int]]:
    nuova_lista = []
    for sotto_lista in lista_numeri:
        mini_lista = []
        for numero in sotto_lista:
            if numero > soglia:
                mini_lista.append(numero*2)
        nuova_lista.append(mini_lista)
    return nuova_lista


def filtra_e_moltiplica1(lista_numeri: list[list[int]], soglia: int) -> list[list[int]]:
    return [list(numero*2 for numero in sotto_lista if numero > soglia) for sotto_lista in lista_numeri]


numeri = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
soglia = 3
print(filtra_e_moltiplica(numeri, soglia))
print(filtra_e_moltiplica1(numeri, soglia))


