'''
Tema: Matrici quadrate
Obiettivo: Lavorare con indici riga/colonna specifici
 
Nome: Somma diagonali
 
Traccia:
Scrivi una funzione somma_diagonali(matrice: list[list[int]]) -> tuple[int, int] che restituisca una tupla con:
 
* Somma della diagonale principale (dall’alto a sinistra al basso a destra)
* Somma della diagonale secondaria (dall’alto a destra al basso a sinistra)
 
Esempio:
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
 
# output atteso
(15, 15)  # diagonale principale: 1+5+9=15, diagonale secondaria: 3+5+7=15
'''

def somma_diagonali(matrice: list[list[int]]) -> tuple[int, int]:
    somma_diagonale_principale = 0
    somma_diagonale_secondaria = 0
    for i in range(len(matrice)):
        somma_diagonale_principale += matrice[i][i]
    for i in range(len(matrice)):
        somma_diagonale_secondaria += matrice[i][len(matrice)-1 -i]

    return (somma_diagonale_principale, somma_diagonale_secondaria)


matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
 
print(somma_diagonali(matrice))
    