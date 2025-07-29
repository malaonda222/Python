'''
Traccia:
Hai un dizionario dove ogni chiave è associata a una lista di valori 
(esempio: corsi e voti). Devi creare una lista di dizionari, dove ogni dizionario 
rappresenta un "record" con i dati combinati da tutte le liste.
'''

def converti_dizionario(dati: dict[str, list[str]]) -> list[dict]:
    lunghezza = len(dati)
    nuova_lista = []
    for i in range(lunghezza):
        record = {}
        for chiave in dati:
            record[chiave] = dati[chiave][i]
        nuova_lista.append(record)

    return nuova_lista




dati = {
    "nome": ["Anna", "Luca", "Antonio"],
    "corso": ["Matematica", "Informatica", "Storia"],
    "voti": [18, 22, 30]
    }


    
print(converti_dizionario(dati))