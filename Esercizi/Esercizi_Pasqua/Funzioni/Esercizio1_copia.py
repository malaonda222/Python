'''Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. 
Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.'''

def converti_tupla(lista_tuple: list[tuple]) -> dict[str, list[int]]:
    nuovo_dict: dict = {}
    for key, value in lista_tuple:
        if key not in nuovo_dict:
            nuovo_dict[key] = [value] 
        else:
            nuovo_dict[key].append(value)
    return nuovo_dict

lista: list = [("a", 3), ("b", 4), ("c", 6), ("c", 7)]
print(converti_tupla(lista))