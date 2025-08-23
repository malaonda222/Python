'''Nome dell’esercizio: Massimo e minimo per colonna
 
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
[(1, 7), (2, 8), (3, 9)]'''

def min_max_per_colonna(matrice: list[list[int]]) -> list[tuple[int, int]]:
    colonne = len(matrice[0])
    lista_tuple = []
    for col in range(colonne):
        colonna = [riga[col] for riga in matrice]
        minimo = min(colonna)
        massimo = max(colonna)
        lista_tuple.append((minimo, massimo))
    return lista_tuple


matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(min_max_per_colonna(matrice))