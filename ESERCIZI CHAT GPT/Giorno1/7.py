'''Traccia:
Scrivi una funzione raggruppa_pari_dispari(numeri: list[int]) -> dict[str, list[int]] che, 
data una lista di numeri, ritorni un dizionario con due chiavi: "pari" e "dispari".
Nella lista "pari" vanno tutti i numeri pari, in "dispari" tutti i numeri dispari.'''

def raggruppa_pari_dispari(numeri: list[int]) -> dict[str, list[int]]:
    new_dict = {"pari": [], "dispari": []}
    for num in numeri:
        if num % 2 == 0:
            new_dict["pari"].append(num) 
        else:
            new_dict["dispari"].append(num)
    return new_dict


numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(raggruppa_pari_dispari(numeri))

