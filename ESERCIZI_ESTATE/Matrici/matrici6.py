'''Scrivi una funzione trasposta che:
prende una matrice rettangolare (es: 3x2)
restituisce la trasposta della matrice (invertendo righe e colonne)'''

def trasposta(matrice: list[list[int]]) -> list[list[int]]:
    matrice_trasposta = []
    colonne = len(matrice[0])
    righe = len(matrice)
    for i in range(colonne):
        nuova_mini_lista = []
        for j in range(righe):
            nuova_mini_lista.append(matrice[j][i])
        matrice_trasposta.append(nuova_mini_lista)
    return matrice_trasposta

matrice = [[1, 2], 
           [3, 4], 
           [5, 6]]
print(trasposta(matrice))

