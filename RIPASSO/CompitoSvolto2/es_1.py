'''Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. 
Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.'''

def converti_tupla(tuples: list[tuple[str, int]]) -> dict[str, list[int]]:
    new_dict = {}
    for chiave, valore in tuples:
        if chiave not in new_dict:
            new_dict[chiave] = [valore]
        else:
            new_dict[chiave].append(valore) 
    return new_dict

tuples = (("vivi", 2), ("vivi", 2), ("ciao", 3), ("come", 4), ("come", 6))
print(converti_tupla(tuples))