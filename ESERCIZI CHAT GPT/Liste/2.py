'''Esercizio 2 – Elementi positivi
Tema: Filtraggio
Obiettivo: Creare una nuova lista con soli elementi positivi
Traccia:
Scrivi una funzione che, data una lista di numeri, ritorni una nuova lista contenente solo i numeri maggiori di 0.
Suggerimento: Prova con list comprehension.'''

def filtraggio(lista_numeri: list[int]) -> list[int]:
    return list(numero for numero in lista_numeri if numero > 0)

def filtraggio1(lista_numeri: list[int]) -> list[int]:
    return list(filter(lambda numero: numero > 0, lista_numeri))

def filtraggio2(lista_numeri: list[int]) -> list[int]:
    nuova_lista = []
    for numero in lista_numeri:
        if numero > 0:
            nuova_lista.append(numero)
    return nuova_lista

lista = [1, 2, -8, -10, -4, 10, 3]
print(filtraggio(lista))
print(filtraggio1(lista))
print(filtraggio2(lista))
