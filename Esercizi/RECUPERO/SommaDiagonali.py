# def sum_primary_diagonal(matrix: list[list[int]]) -> int:
#     somma_diagonali_sx_dx = 0
#     for i in range(len(matrix)): 
#         somma_diagonali_sx_dx += matrix[i][i] 
#     return somma_diagonali_sx_dx

# def sum_secondary_diagonal(matrix: list[list[int]]) -> int:
#     somma_diagonali_dx_sx = 0
#     for i in range(len(matrix)):
#         somma_diagonali_dx_sx += matrix[i][-1 -i]
#     return somma_diagonali_dx_sx


# def sum_primary_diagonal(matrix: list[list[int]]) -> int:
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             if i == j:
#                 somma += matrix[i][j]

# def sum_secondary_diagonal(matrix: list[list[int]]) -> int:
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             if i == j:
#                 somma += matrix[i][-1 -j]


# def diag(m: list[list[int]]) -> int:
#     somma: int = 0
#     somma2: int = 0
#     for i in range(len(m)):
#         somma += m[i][i]
#         somma2 += m[i][len(m) -1 -i]
#     return somma or somma2 

# mat1 = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]
# ]

# mat2 = [
# [2, 8, 9, 5],
# [5, 2, 9, 3],
# [7, 5, 4, 3],
# [8, 4, 2, 6],
# [9, 5, 8, 3]
# ]

# print(sum_primary_diagonal(mat1))
# print(sum_secondary_diagonal(mat1))

# print(sum_primary_diagonal(mat2))
# print(sum_secondary_diagonal(mat2))


def primary_diagonal(m: list[list[int]]) -> int:
    somma_diagonale_dx = 0
    for i in range(len(m)):
        somma_diagonale_dx += m[i][i]
    return somma_diagonale_dx

def secondary_diagonal(m: list[list[int]]) -> int:
    somma_diagonale_sx = 0
    for i in range(len(m)):
        somma_diagonale_sx += m[i][len(m) -1 - i]
    return somma_diagonale_sx

mat1 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

mat2 = [
[2, 8, 9, 5],
[5, 2, 9, 3],
[7, 5, 4, 3],
[8, 4, 2, 6],
[9, 5, 8, 3]
]

print(primary_diagonal(mat1))
print(secondary_diagonal(mat2))

