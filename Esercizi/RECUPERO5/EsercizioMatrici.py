from random import randint

'''1.A'''
#genero una matrice di dimensione n x n 
def genera(n: int) -> int:
    #creo una lista vuota per la matrice
    matrix: list[list[int]] = []
    #creo un ciclo esterno che scorra la righe
    for r in range(n):
        #creo una riga vuota
        row: list[int] = []
        #genero il primo elemento della riga
        primo_elemento = randint(0, 13)
        row.append(primo_elemento)
        #ciclo interno: aggiungo altri n-1 elementi
        while len(row) < n:
            elemento = randint(0, 13)
            if elemento != primo_elemento:
                row.append(elemento)
        #aggiungo la riga alla matrice
        matrix.append(row)
    #ritorno la matrice
    return matrix

'''1.B.'''
def printMAT(matrix: list[list[int]]) -> None:
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            print(f"{matrix[r][c]:<5}", end="")
        print("\n")

'''1.C.'''
def calcolaCarico(matrix: list[list[int]], r: int, c: int):
    somma_riga = 0
    somma_colonna = 0
    for j in range(len(matrix[r])):
        somma_riga += matrix[r][j] 
    for i in range(len(matrix)):
        somma_colonna += matrix[i][c]
    
    k = (somma_riga - somma_colonna)
    return k

'''1.D.'''
def caricoNullo(matrix: list[list[int]]) -> list[tuple]:
    coppie_nulle: list[tuple] = []
    righe = len(matrix)
    colonne = len(matrix[0]) if righe > 0 else 0

    for r in range(righe):
        for c in range(colonne):
            if calcolaCarico(matrix, r, c) == 0:
                coppie_nulle.append((r, c))
    print(f"Numero tuple a carico nullo -> {len(coppie_nulle)}")
    return f"Coppie a carico nullo -> {coppie_nulle}"


'''1.E.'''
def caricoMax(matrix: list[list[int]]):
    righe = len(matrix)
    colonne = len(matrix[0])
    max_carico = None
    max_posizione = (0, 0)

    for r in range(righe):
        for c in range(colonne):
            calcolo = calcolaCarico(matrix, r, c)
            if max_carico is None or calcolo > max_carico:
                max_carico = calcolo 
                max_posizione = (r, c)
    
    return max_posizione, max_carico


'''1.F.'''
def caricoMin(matrix: list[list[int]]):
    righe = len(matrix)
    colonne = len(matrix[0])
    min_carico = None 
    min_posizione = (0, 0)

    for r in range(righe):
        for c in range(colonne):
            calcolo = calcolaCarico(matrix, r, c)
            if min_carico is None or calcolo < min_carico:
                min_carico = calcolo 
                min_posizione = (r, c)
    return min_posizione, min_carico


if __name__ == '__main__':

    matrice2 = genera(5)
    print("Matrice (lista):")
    for riga in matrice2:
        print(riga)
    print("\nMatrice (grafico):")
    printMAT(matrice2)

    print("\nPosizioni a carico nullo:")
    print(caricoNullo(matrice2))

    (rmax, cmax), max_carico = caricoMax(matrice2)
    print(f"CaricoMax: ({rmax}, {cmax}) con valore: {max_carico}")
    print(f"Valore calcolaCarico: {calcolaCarico(matrice2, rmax, cmax)}")

    (rmin, cmin), min_carico = caricoMin(matrice2)
    print(f"CaricoMin: ({rmin}, {cmin}) con valore {min_carico}")
    print(f"Valore calcolaCarico: {calcolaCarico(matrice2, rmin, cmin)}")


     # matrice = genera(3)
    # for riga in matrice:
    #     print(riga)
    
    # printMAT(matrice)

    # matrice1 = genera(5)
    # printMAT(matrice1)
    # r = 2
    # c = 1
    # print(f"Carico in posizione({r}, {c}): {calcolaCarico(matrice1, r, c)}")
    # print(caricoNullo(matrice1))
    # print(caricoMax(matrice1))
    # print(caricoMin(matrice1))