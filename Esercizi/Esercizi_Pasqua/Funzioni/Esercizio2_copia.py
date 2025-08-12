'''Scrivi una funzione che accetti una lista di numeri e ritorni 
la somma dei numeri che sono divisibili sia per 2 che per 3.'''

def somma_numeri(lista_num: list[int|float]) -> float:
    somma_numeri = 0
    for num in lista_num:
        if num % 2 == 0 and num % 3 == 0:
            somma_numeri += num 
    return f"Somma dei numeri divisibili per 2 e per 3: {somma_numeri}"


print(somma_numeri([30, 1, 4, 15, 70, 19.09, 6, 12]))
print(somma_numeri([7, 18, 26, 3333, 59]))