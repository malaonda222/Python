def generaMAT(n: int) -> list[list[int]]:
    mat: list[list[int]] = []
    for r in range(n):
        row: list[int] = []
        for c in range(n):
            x: int = (r+1) * (c+1)
            row.append(x)
        mat.append(row)
    return mat 

def printMAT(mat: list[list[int]]) -> None:
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            print(f"{mat[r][c]:<5}", end="")
        print("\n")
    
if __name__ == '__main__':
    matrice: list[list[int]] = generaMAT(10)
    printMAT(matrice)
    