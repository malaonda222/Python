'''Scrivi una funzione trasposta(matrice: list[list[int]]) -> list[list[int]] che 
restituisca la matrice trasposta, cioè una nuova matrice dove le righe diventano colonne e le colonne diventano righe.
 
Esempio:
matrice = [
    [1, 2, 3],
    [4, 5, 6]
]
 
# output atteso
[
    [1, 4],
    [2, 5],
    [3, 6]
]
'''

def matrice_trasposta(matrice: list[list[int]]) -> list[list[int]]:
    nuova_matrice = []
    colonne = len(matrice[0])
    righe = len(matrice)
    for i in range(colonne):
        nuova_riga = []
        for j in range(righe):
            nuova_riga.append(matrice[j][i])
        nuova_matrice.append(nuova_riga)
    return nuova_matrice


matrice = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrice_trasposta(matrice))


