'''Esercizio 4 - Inversione lista
Tema: Manipolazione lista
Obiettivo: Invertire una lista
Traccia:
Scrivi una funzione che prenda una lista e ritorni una nuova lista con gli elementi in ordine inverso.
Suggerimento: Prova con slicing [::-1].'''

from typing import Any

def inversione(lista: list[Any]) -> list[Any]:
    return lista[::-1]

def inversione1(lista: list[Any]) -> list[Any]:
    lista_invertita = []
    for i in range(len(lista)-1, -1, -1):
        lista_invertita.append(lista[i])
    return lista_invertita


lista_caratteri = [1, 3, 5, 6, 9, "Cicoria", "Pollo", 0.90, True]
print(inversione(lista_caratteri))
print(inversione1(lista_caratteri))
