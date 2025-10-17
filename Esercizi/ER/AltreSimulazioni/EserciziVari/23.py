'''
Filtra e raddoppia dispari
 
Nome dell’esercizio: filter_and_double_odd
Scrivi una funzione che:
* Prende in input una lista di numeri interi nums e una soglia limite.
* Filtra solo i numeri dispari maggiori o uguali a limite.
* Restituisce una lista con ogni numero filtrato raddoppiato.
 
Esempio:
filter_and_double_odd([2, 3, 5, 8, 11], 5)
# ➜ [10, 22]
'''

def filter_and_double_odd(nums: list[int], soglia: int) -> list[int]:
    return [num*2 for num in nums if num >= soglia and num % 2 != 0]


def filter_and_double_odd1(nums: list[int], soglia: int) -> list[int]:
    new_list = []
    for num in nums:
        if num >= soglia and num % 2 != 0:
            new_list.append(num*2)
    return new_list


print(filter_and_double_odd([2, 3, 5, 8, 11], 5))
print(filter_and_double_odd1([2, 3, 5, 8, 11], 5))
