'''Filtra solo le parole che compaiono una sola volta
Tema: Liste, conteggi, filter, lambda
Obiettivo: Isolare gli elementi unici in una lista (quelli che compaiono esattamente una volta)
 
Nome dell’esercizio: elementi_unici_assoluti
 
Traccia:
Scrivi una funzione che prende una lista di parole e restituisce una nuova lista 
contenente solo le parole che appaiono una sola volta, nell’ordine originale.
 
# Esempio:
parole = ["ciao", "mondo", "ciao", "python", "ciao", "codice", "python", "ciao", "logica"]
 
# Output atteso:
["mondo", "codice", "logica"]'''

from typing import Callable 

def elementi_unici_assoluti(parole: list) -> list[str]:
    parole_viste = set()
    parole_duplicate = set()
    for parola in parole:
        if parola not in parole_viste:
            parole_viste.add(parola)
        else:
            parole_duplicate.add(parola)
    return [parola for parola in parole if parola not in parole_duplicate]

parole = ["ciao", "mondo", "ciao", "python", "ciao", "codice", "python", "ciao", "logica"]
print(elementi_unici_assoluti(parole))


def elementi_unici_assoluti2(parole: list) -> list[str]:
    occorrenze = {}
    lista_unici = []
    for element in parole:
        if element not in occorrenze:
            occorrenze[element] = 1
        else:
            occorrenze[element] += 1
    for key, value in occorrenze.items():
        if value == 1:
            lista_unici.append(key)
    return lista_unici

parole = ["ciao", "mondo", "ciao", "python", "ciao", "codice", "python", "ciao", "logica"]
print(elementi_unici_assoluti2(parole))


def elementi_unici_assoluti3(parole: list) -> list[str]:

    parole_uniche: list[str] = list(filter(lambda parola: parole.count(parola) == 1, parole))
    return parole_uniche

    # oppure 
    conteggio = {}
    for parola in parole:
        if parola not in conteggio:
            conteggio[parola] = 1
        else:
            conteggio[parola] += 1
    return list(filter(lambda parola: conteggio[parola] == 1, parole))

print(elementi_unici_assoluti3(parole))

