'''Data una lista di numeri, crea una nuova lista che contenga 
solo i numeri pari.'''

def numeri_pari(numeri: list[int]) -> list[int]:
    return [num for num in numeri if num % 2 == 0]


numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeri_pari(numeri))