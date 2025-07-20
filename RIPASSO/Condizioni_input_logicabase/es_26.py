'''Scrivi una funzione two_sum(lst, target) che ritorna gli indici 
di due numeri nella lista che sommati danno target.'''

def two_sum(lst: list, target: int) -> tuple:
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                print(f"{i, j}")
    
two_sum([2, 7, 11, 15], 9)