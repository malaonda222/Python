'''Data una lista di numeri, crea una nuova lista che contenga il 
quadrato di ogni numero.'''

def quadrato(numeri: list[int]) -> list[int]:
    return [num**2 for num in numeri]


numeri = [1, 2, 3, 4, 5]
print(quadrato(numeri))