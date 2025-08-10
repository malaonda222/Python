'''Crea una funzione che accetta un numero variabile di argomenti.'''

from typing import Union

def numero_variabile(*args: Union[int|float|str|bool]):
    if not args:
        print("Errore, nessun elemento inserito.")
    else:
        print([arg for arg in args])

numero_variabile(1, 4, "ciao", 10, True)