'''Esercizio 5 - Elementi unici
Tema: Set e liste
Obiettivo: Ottenere gli elementi senza duplicati
Traccia:
Scrivi una funzione che ritorni una lista contenente solo gli elementi unici di una lista iniziale (cioè senza ripetizioni).
Suggerimento: Puoi usare un set o controllare manualmente.'''

def elementi_unici(lista: list[int]) -> list[int]:
    return list({element for element in lista})

def elementi_unici1(lista: list[int]) -> list[int]:
    unici = []
    for elemento in lista:
        if elemento not in unici:
            unici.append(elemento)
    return unici

def elementi_unici2(lista: list[int]) -> list[int]:
    unici = []
    [unici.append(element) for element in lista if element not in unici]
    return unici




lista_numeri = [1, 3, 3, 6, 7, 9, 0, 0]
print(elementi_unici(lista_numeri))
print(elementi_unici1(lista_numeri))
print(elementi_unici2(lista_numeri))