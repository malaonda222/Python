'''Esercizio 2'''
#funzione che ritorni un dizionario che mappa ogni elemento alla sua frequenza nella lista
def frequency_dict(elements:list) -> dict:
    dizionario_frequenze = {}
    for item in elements:
        if item in dizionario_frequenze:
            dizionario_frequenze[item] += 1 
        else:
            dizionario_frequenze[item] = 1
    
    return dizionario_frequenze