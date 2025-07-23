'''
Traccia:
Scrivi una funzione ricorsiva che prende un dizionario e restituisce 
la somma di tutti i valori che sono numeri interi o float. Ignora gli altri valori.
'''

def recursive_sum(diz: dict) -> int:
    if not diz:
        return 0
    
    keys = list(diz.keys())
    key = keys[0]
    value = diz[key]
    resto = {k: diz[k] for k in keys[1:]}

    
    if isinstance(value, (int, float)):
        return value + recursive_sum(resto)
    else:
        recursive_sum(resto)   
        
print("La somma dei valori del dizionario è: ")
print(recursive_sum({"a": 1, "b": 2, "c": 3}))