'''Traccia:
Scrivi una funzione conteggio_elementi(lista: list[Any]) -> dict[Any, int] 
che ritorni un dizionario con gli elementi della lista come chiavi e il numero di occorrenze come valori.
 
Input:
elementi = ["apple", "banana", "apple", "orange", "banana", "apple"]'''

from typing import Any
def conteggio_elementi(lista: list[Any]) -> dict[Any, int]:
    frequenze = {}
    for el in lista:
        if el not in frequenze:
            frequenze[el] = 0
        frequenze[el] += 1
    return frequenze


def conteggio_elementi2(lista: list[Any]) -> dict[Any, int]:
    return {elemento: lista.count(elemento) for elemento in set(lista)}




elementi = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(conteggio_elementi(elementi))
print(conteggio_elementi2(elementi))
