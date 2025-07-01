'''Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. 
Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.'''

def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    nuovo_dict = {}
    for key, value in tuples:
        if key not in nuovo_dict:
            nuovo_dict[key] = [value]
        else:
            nuovo_dict[key].append(value) 
    return nuovo_dict