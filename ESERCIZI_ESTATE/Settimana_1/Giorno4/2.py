'''Dato un dizionario, stampa tutte le chiavi e i valori.'''

dizionario: dict = {"a": 1, "b": 2, "c": 3, "e": 4}
for key, value in dizionario.items():
    print(key, value)