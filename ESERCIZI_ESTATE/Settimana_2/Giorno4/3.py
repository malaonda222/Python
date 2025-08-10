'''Usa reduce per calcolare il prodotto di una lista.'''

from functools import reduce

def prodotto(a: int, b: int) -> int:
    return a*b

def reducing(lista: list[int]) -> int:
    risultato = reduce(prodotto, lista)
    return risultato

print(reducing([3, 4, 5, 2, 4, 20]))

def somma(a: int, b: int) -> int:
    return a + b

def somma2(lista_numeri: list[int]) -> int:
    risultato = reduce(somma, lista_numeri)
    return risultato

print(somma2([3, 4, 6, 7, 333, 4]))