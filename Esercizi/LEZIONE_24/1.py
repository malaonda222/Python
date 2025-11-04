'''Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.
print(merge_dictionaries({'x': 5}, {'x': -5})) '''

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    for key, value in dict2.items():
        if key in dict1:
            dict1[key] += value
        else:
            dict1[key] = value 
    return dict1

