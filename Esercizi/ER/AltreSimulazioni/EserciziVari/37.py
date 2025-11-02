'''Scrivi una funzione chiamata filter_and_sum che prenda una lista di 
numeri interi e un valore minimo, e restituisca la somma di tutti i 
numeri che sono maggiore o uguale al valore minimo. 
Se non ci sono numeri che soddisfano la condizione, restituisci 0.'''


def filter_and_sum(nums: list[int], min_value: int) -> int:
    somma_totale = 0
    for num in nums: 
        if num >= min_value:
            somma_totale += num 
    if not somma_totale:
        return 0
    else: 
        return somma_totale
    
    # oppure
    # somma_totale = sum(num for num in nums if num >= min_value)
    #       return somma_totale if somma_totale > 0 else 0

print(filter_and_sum([4, 6, 13, 2, 55, 6, 34], 30))
