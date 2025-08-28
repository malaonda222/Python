'''
Traccia:
Scrivi una funzione trasposta(matrice) che ritorni la matrice trasposta 
(righe ↔ colonne) 
utilizzando list comprehension.
 
matrice = [
    [1, 2, 3],
    [4, 5, 6]
]'''


def trasposta(matrice: list[list[int]]) -> list[list[int]]:
    righe = len(matrice)
    colonne = len(matrice[0])
    matrice_trasposta = []
    for j in range(colonne):
        nuova_riga = []
        for i in range(righe):
            nuova_riga.append(matrice[i][j])
        matrice_trasposta.append(nuova_riga)
    return matrice_trasposta

def trasposta2(matrice: list[list[int]]) -> list[list[int]]:
    return [[matrice[riga][colonna] for riga in range(len(matrice))] for colonna in range(len(matrice[0]))]

matrice = [
    [1, 2, 3],
    [4, 5, 6]
]
print(trasposta(matrice))
print(trasposta2(matrice))