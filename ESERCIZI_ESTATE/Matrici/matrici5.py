'''Scrivi una funzione somma_maggiori_di che:
prende una matrice (lista di liste di int)
prende una soglia k
restituisce la somma di tutti i numeri della matrice maggiori di k'''

def somma_maggiori_di(matrice: list[list[int]], k: int) -> int:
    somma = 0
    for lista in matrice:
        for numero in lista:
            if numero > k:
                somma += numero 
    return somma


def somma_maggiori_di_(matrice: list[list[int]], k: int) -> int:
    return sum(numero for lista in matrice for numero in lista if numero > k)

print(somma_maggiori_di([[1, 2], [3, 4], [5, 6]], 2))
print(somma_maggiori_di_([[1, 2], [3, 4], [5, 6]], 2))