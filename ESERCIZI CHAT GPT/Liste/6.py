'''Esercizio 6 - Intersezione di liste
Tema: Operazioni tra liste
Obiettivo: Trovare elementi comuni
Traccia:
Scrivi una funzione che, date due liste, ritorni una lista con gli elementi comuni ad entrambe.'''

from typing import Any 

def elementi_comuni(lista1: list[Any], lista2: list[Any]) -> list[Any]:
    return list(elemento for elemento in lista1 if elemento in lista2)

def elementi_comuni1(lista1: list[Any], lista2: list[Any]) -> list[Any]:
    comuni = []
    for elemento in lista1:
        if elemento in lista2 and elemento not in comuni:
            comuni.append(elemento)
    return comuni

lista1 = ["ciao", 4, 5, 10]
lista2 = ["come", 5, 10, 43, 6, "ciao"]
print(elementi_comuni(lista1, lista2))