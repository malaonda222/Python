'''Traccia:
Scrivi una funzione somma_diagonale(matrice) che, data una matrice quadrata, 
ritorni la somma degli elementi della diagonale principale.
 
Input:
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]'''

def somma_diagonale(matrice: list[list[int]]) -> int:
    somma = 0
    for i in range(len(matrice)):
        somma += matrice[i][i]
    return somma 

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(somma_diagonale(matrice))