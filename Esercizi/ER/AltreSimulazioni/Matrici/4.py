'''
Tema: Matrici (liste di liste)
Obiettivo: Calcolare i valori minimi delle colonne
 
Nome dell’esercizio: Minimo per colonna
 
Traccia:
Scrivi una funzione minimo_per_colonna(matrice: list[list[int]]) -> list[int] che prende una matrice di 
numeri e restituisce una lista contenente il valore minimo di ogni colonna.
 
Esempio:
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
 
Suggerimento:
* Non utilizzare funzioni built-in
'''

def minimo_per_colonna1(matrice: list[list[int]]) -> list[int]:
    lista_minimi = []
    num_colonne = len(matrice[0])

    for colonna in range(num_colonne):
        minimo = matrice[0][colonna]
        for riga in matrice:
            valore = riga[colonna]
            if valore < minimo:
                minimo = valore
        lista_minimi.append(minimo)
    return lista_minimi



def minimo_per_colonna(matrice: list[list[int]]) -> list[int]:
    minimi = []
    numero_colonne = len(matrice[0])

    for colonna in range(numero_colonne):
        minimo = matrice[0][colonna]
        for riga in matrice:
            if riga[colonna] < minimo:
                minimo = riga[colonna]
        minimi.append(minimo)
    return minimi 

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(minimo_per_colonna(matrice))
print(minimo_per_colonna1(matrice))

