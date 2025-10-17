'''
Tema: Matrici
Obiettivo: Capire come scambiare righe e colonne
 
Nome: Trasposta di una matrice
 
Traccia:
Scrivi una funzione trasposta(matrice: list[list[int]]) -> list[list[int]] che 
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

def trasposta(matrice: list[list[int]]) -> list[list[int]]:
    num_colonne = len(matrice[0])
    matrice_trasposta = []

    for colonna in range(num_colonne): #oppure range(len(matrice[0])) se non si crea la variabile num_colonne
        sottolista = []

        for riga in matrice:
            sottolista.append(riga[colonna])

        matrice_trasposta.append(sottolista)

    return matrice_trasposta


matrice = [
    [1, 2, 3],
    [4, 5, 6]
]
print(trasposta(matrice))