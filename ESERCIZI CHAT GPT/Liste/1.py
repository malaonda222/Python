'''Esercizio 1 - Somma e prodotto
Tema: Operazioni base su liste
Obiettivo: Sommare tutti gli elementi di una lista e calcolare il prodotto
Traccia:
Scrivi una funzione che, data una lista di numeri interi, ritorni la somma e il prodotto di tutti gli elementi.
Suggerimento: Usa un ciclo for o le funzioni sum() e reduce().'''

from functools import reduce 

def somma_prodotto(lista_numeri: list[int]) -> tuple:
    somma = 0
    prodotto = 1
    for element in lista_numeri:
        somma += element
        prodotto *= element 
    return somma, prodotto

def somma_prodotto1(lista_numeri: list[int]) -> tuple:
    somma = reduce(lambda a, b: a+b, lista_numeri)
    prodotto = reduce(lambda a, b: a*b, lista_numeri)
    return somma, prodotto


lista_numeri = [1, 2, 3, 4, 5]
print(somma_prodotto(lista_numeri))
print(somma_prodotto1(lista_numeri))
