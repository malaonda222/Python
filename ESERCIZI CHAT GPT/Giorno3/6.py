'''
Traccia:
Hai un grafo rappresentato da una matrice di adiacenza (0 = nessun arco, 1 = arco).
Esempio:
 
grafo = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
]
 
Scrivi una funzione matrice_a_archi(grafo) che ritorni una lista di tuple (i, j) 
che rappresentano gli archi. Usa comprehension.
 
Output atteso con l’esempio:
[(0, 1), (1, 0), (1, 2), (2, 1)]
'''

def matrice_a_archi(grafo: list[list[int]]) -> list[tuple]:
    lista_tuple = []
    righe = len(grafo)
    colonne = len(grafo[0])
    for i in range(righe):
        for j in range(colonne):
            if grafo[i][j] == 1:
                lista_tuple.append((i, j))
    return lista_tuple
    
grafo = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
]
print(matrice_a_archi(grafo))
