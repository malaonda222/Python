'''Tema: Liste e funzioni filter/map - Trasformazione e filtraggio di elementi
Obiettivo: Dato un elenco di numeri, restituire una nuova lista contenente solo i quadrati dei numeri pari.
Nome dell’esercizio: quadrati_dei_pari
Traccia:
Scrivi una funzione che prenda una lista di numeri interi e restituisca una lista con i quadrati dei numeri pari presenti nella lista originale.
Suggerimento: puoi usare filter() per selezionare i numeri pari e map() per calcolarne il quadrato, oppure una list comprehension.'''


def quadrati_dei_pari(lista_numeri: list[int]) -> list[int]:
    return [num**2 for num in lista_numeri if num % 2 == 0]


def quadrato_dei_pari2(lista_numeri: list[int]) -> list[int]:
    numeri_pari: list = list(filter(lambda x: x % 2 == 0, lista_numeri))
    quadrati: list = list(map(lambda x: x**2, numeri_pari))
    return quadrati


numeri = [3, 5, 6, 7, 4, 555, 6, 9]
print(quadrati_dei_pari(numeri))
print(quadrato_dei_pari2(numeri))



