'''Calcolare il prodotto della somma dei valori che hanno indice pari di una lista con la somma dei valori che hanno indice dispari'''

def prodotto_valori(lista_numeri: list[int]) -> int:
    somma_pari = 0
    somma_dispari = 0
    for i in range(len(lista_numeri)):
        if i % 2 == 0:
            somma_pari += lista_numeri[i]
        else:
            somma_dispari += lista_numeri[i] 
    prodotto = somma_dispari * somma_pari
    return prodotto 

print(prodotto_valori([1, 4, 2222, 3, 4, 6, 8, 88, 903]))