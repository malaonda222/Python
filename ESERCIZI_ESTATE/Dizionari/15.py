'''Traccia:
Data una matrice (lista di liste di numeri), restituisci una lista con la somma di ogni riga.
 
Input:
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]'''

def matrice(matrix: list[list[int]]) -> list[int]:
    lista_matrix = []
    for riga in matrix:
        somma = 0
        for element in riga:
            somma += element
        lista_matrix.append(somma)
    return lista_matrix

def matrice2(matrix: list[list[int]]) -> list[int]:
    lista_matrix2 = []
    for riga in matrix:
        somma = sum(element for element in riga)
        lista_matrix2.append(somma)
    return lista_matrix2

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrice(matrix))
print(matrice2(matrix))
        