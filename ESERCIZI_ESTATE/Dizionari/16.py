'''Data una matrice (lista di liste), restituisci la sua trasposta, cioè una nuova matrice 
in cui:
* la prima riga della trasposta è la prima colonna della matrice originale
* la seconda riga della trasposta è la seconda colonna della matrice originale
* e così via...
 
Input:
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]'''

def matrix(lista_matrici: list[list[int]]) -> list[list[int]]:
    new_list = []
    righe = len(lista_matrici)
    colonne = len(lista_matrici[0])
    for j in range(colonne):
        nuova_riga = []
        for i in range(righe):
            nuova_riga.append(lista_matrici[i][j])
        new_list.append(nuova_riga)
    return new_list

