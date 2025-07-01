'''2) Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
dato valore intero definito threshold.'''

from typing import Union

def moltiplica(list_1: list[int]):
    threshold: int = 50
    prodotto = 1
    for item in list_1:
        if item < threshold:
            prodotto *= item 
    return prodotto

lista_3 = (2, 5, 88, 4, 7, 9)
print(moltiplica(lista_3))


def product(lista_interi: list[Union[int, float]], soglia:int = 50) -> int:
    prodotto_cumulato: int = 1
    for element in lista_interi:
        if type(element) != int: #o usiamo Union oppure type(element) != int
            continue 
        if element < soglia:
            prodotto_cumulato *= element 
    
    return prodotto_cumulato



