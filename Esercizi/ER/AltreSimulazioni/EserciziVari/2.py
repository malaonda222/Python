'''Scrivi una funzione chiamata double_and_filter che prende:
una lista di numeri interi nums
un valore massimo max_val (intero)

La funzione deve:
Moltiplicare ogni numero della lista per 2.
Filtrare solo i numeri doppiati che sono minori o uguali a max_val.
Restituire una stringa con questi numeri, separati da uno spazio (" "), nell’ordine originale.'''

def double_and_filter(nums: list[int], max_val: int) -> str:
    lista_doppi = [num*2 for num in nums]
    filtrati = [str(num) for num in lista_doppi if num <= max_val]
    return " ".join(filtrati)


def double_and_filter1(nums: list[int], max_val: int) -> str:
    filtro = [str(num * 2) for num in nums if num * 2 <= max_val]
    return " ".join(filtro)


numeri = [3, 5, 6, 3, 4]
max_val = 8
 

print(double_and_filter(numeri, max_val))
print(double_and_filter1(numeri, max_val))

nums = [4, 6, 3]
max_val = 10

print(double_and_filter1(nums, max_val))
print(double_and_filter(nums, max_val))
