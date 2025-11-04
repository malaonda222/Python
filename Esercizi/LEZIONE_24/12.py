'''Scrivi una funzione che prenda un dizionario e un valore, e ritorni la
prima chiave che corrisponde a quel valore, o None se il valore non è 
presente.'''

def trova_chiave_per_valore(dizionario: dict[str, int], valore: int) -> str:
    risultato = None
    for key, value in dizionario.items():
        if value == valore:
            risultato = key 
    
    return risultato

print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200))
print(trova_chiave_per_valore({'k1': 'v1', 'k2': 'v2'}, 'v3'))
