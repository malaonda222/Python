'''Scrivi una funzione che prende una lista di numeri e ritorna un 
dizionario che classifica i numeri in liste separate per numeri pari e dispari.'''

def classifica_numeri(lista: list[int]) -> dict[str: list[int]]:
    new_dict: dict = {"pari": [], "dispari": []}
    
    for numero in lista:
        if numero % 2 == 0:
            new_dict["pari"].append(numero)
        else:
            new_dict["dispari"].append(numero)
    
    return new_dict

print(classifica_numeri([1, 2, 3, 4, 5, 6]))