'''Tema: Matrici (liste di liste)
Obiettivo: Sommare i valori di ciascuna riga e di ciascuna colonna
 
Nome dell’esercizio: Somma righe e colonne
 
Traccia:
Scrivi due funzioni:
 
* somma_righe(matrice: list[list[int]]) -> list[int] → restituisce una lista con la somma di ciascuna riga.
* somma_colonne(matrice: list[list[int]]) -> list[int] → restituisce una lista con la somma di ciascuna colonna.
 
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]'''

def somma_righe(matrice: list[list[int]]) -> list[int]:
    lista_somme_righe = []
    for riga in matrice:
        somma = 0
        for elemento in riga:
            somma += elemento 
        lista_somme_righe.append(somma)
    return lista_somme_righe

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(somma_righe(matrice))


def somma_colonne(matrice: list[list[int]]) -> list[int]:
    lista_somme_colonne = []
    colonne = len(matrice[0])
    for col in range(colonne): 
        somma_colonne = 0
        for riga in matrice:
            somma_colonne += riga[col] 
        lista_somme_colonne.append(somma_colonne)
    return lista_somme_colonne

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(somma_colonne(matrice))