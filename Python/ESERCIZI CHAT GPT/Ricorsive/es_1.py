'''Scrivi una funzione ricorsiva che calcoli la somma di tutti
i numeri interi da 1 a n.'''

def recursiveSum(numero:int) -> int:
    if numero == 1:
        return 1
    if numero == 0: 
        return 0
    else:
        return int(numero + (recursiveSum(numero - 1)))