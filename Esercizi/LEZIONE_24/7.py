'''Scrivi una funzione che, data una lista, ritorni un dictionary che 
mappa ogni elemento alla sua frequenza nella lista.'''

from typing import Any

def frequency_dict(elements: list[Any]) -> dict|str:
    if not elements:
        return "Lista di elementi vuota"
    risultato: dict = {}
    for element in elements:
        if element not in risultato:
            risultato[element] = 1
        else:
            risultato[element] += 1
    if not risultato:
        return {}
    else:
        return risultato