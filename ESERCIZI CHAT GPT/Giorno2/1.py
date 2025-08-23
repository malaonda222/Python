'''Traccia:
Scrivi una funzione raggruppa_per_decina(numeri: list[int]) -> dict[int, list[int]] che, 
data una lista di numeri, ritorni un dizionario in cui le chiavi sono le decine (0, 10, 20, …) e 
i valori sono le liste dei numeri che appartengono a quella decina.
 
Input:
numeri = [3, 7, 12, 15, 21, 29, 33, 37, 120, 1458]'''

def raggruppa_per_decina(numeri: list[int]) -> dict[int, list[int]]:
    new_dict = {}
    for num in numeri:
        decina = (num // 10) * 10
        if num not in new_dict:
            new_dict[decina] = []
        new_dict[decina].append(num)
    return new_dict


numeri = [3, 7, 12, 15, 21, 29, 33, 37, 120, 1458]
print(raggruppa_per_decina(numeri))