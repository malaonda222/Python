'''Scrivi una funzione che accetti una lista di numeri e ritorni 
la somma dei numeri che sono divisibili sia per 2 che per 3.'''

def somma_numeri(lista: list[int]) -> int:
    somma = 0
    for element in lista:
        if element % 2 == 0 and element % 3 == 0:
            somma += element 
    return somma

print(somma_numeri([3, 6, 15, 4, 9 , 506, 7384]))