'''
Tema: Matrici
Obiettivo: Calcolare massimo e minimo per ogni colonna
 
Nome dell’esercizio: Massimo e minimo per colonna
 
Traccia:
Scrivi una funzione min_max_per_colonna(matrice: list[list[int]]) -> list[tuple[int, int]] 
che restituisca per ogni colonna una tupla (minimo, massimo).
 
Esempio:
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
 
# output atteso
[(1, 7), (2, 8), (3, 9)]
'''

def min_max_per_colonna(matrice: list[list[int]]) -> list[tuple[int, int]]:
    lista_tuple = []
    num_colonne = len(matrice[0])

    for colonna in range(num_colonne):
        minimo = matrice[0][colonna]
        massimo = matrice[0][colonna]
        
        for riga in matrice:
            if riga[colonna] < minimo:
                minimo = riga[colonna]
            if riga[colonna] > massimo:
                massimo = riga[colonna]
        lista_tuple.append((minimo, massimo))
    return lista_tuple

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(min_max_per_colonna(matrice))