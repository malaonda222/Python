'''Data una matrice (lista di liste), appiattiscila in un’unica lista.'''

def matrix(matrice: list[list[int]]) -> list[int]:
    return [num for riga in matrice for num in riga]


matrice = [[1, 2], [3, 4], [5, 6]]
print(matrix(matrice))
