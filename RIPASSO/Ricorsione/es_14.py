'''Traccia:
Scrivi una funzione ricorsiva che prende un set di elementi (di qualsiasi tipo) 
e conta quante stringhe contengono almeno una vocale (a, e, i, o, u, anche maiuscole).
Ignora tutti gli elementi non stringa.'''

def conta_vocale(set1: set) -> int:
    set1_lista = list(set1)
    if not set1:
        return 0

    inizio = set1_lista[0]
    fine = set(set1_lista[1:])
    vocali = {"a", "e", "i", "o", "u"}
   
    if isinstance(inizio, str) and any(c.lower() in vocali for c in inizio):
        return 1 + conta_vocale(fine)
    else:
        return conta_vocale(fine)
    



set1: set = {"asilo", "3", "ciao", "frnvg"}
print(conta_vocale(set1))






def conta_stringhe(set1: set) -> int:
    set1_list = list(set1)
    if not set1_list:
        return 0 
    vocali = {"a", "e", "i", "o", "u"}
    inizio = set1_list[0]
    fine = set(set1_list[1:])

    if isinstance(inizio, str) or any(c.lower() in vocali for c in inizio):
        return 1 + conta_stringhe(fine)
    else:
        return conta_stringhe(fine)







