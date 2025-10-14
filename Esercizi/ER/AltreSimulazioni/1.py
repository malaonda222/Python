'''Esercizio: filter_and_join
Scrivi una funzione chiamata filter_and_join che prende in input:
una lista di numeri interi nums
un valore minimo min_val (intero)
La funzione deve:
Filtrare tutti i numeri nella lista che sono maggiore o uguale a min_val.
Convertire i numeri filtrati in stringhe.
Restituire una stringa contenente tutti i numeri filtrati concatenati, separati da un punto e virgola ";".'''

def filter_and_join(nums: list[int], min_val: int) -> str:
    stringa = []
    for num in nums:
        if num >= min_val:
            stringa.append(str(num))
    return ";".join(stringa)


def filter_and_join1(nums: list[int], min_val: int) -> str:
    return ";".join(str(num) for num in nums if num >= min_val)


def filter_and_join2(nums: list[int], min_val: int) -> str:
    stringa = [str(num) for num in nums if num >= min_val]
    return ";".join(stringa)


numeri = [1, 4, 5, 3, 0]
valore_minimo = 2 
print(filter_and_join(numeri, valore_minimo))
print(filter_and_join2(numeri, valore_minimo))