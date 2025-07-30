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
print()


def diz_converti(infos: dict[str, list[str|int]]) -> list[dict]:
    new_list = []
    n = len(infos["nome"])
    for i in range(n):
        record = {"nome": infos["nome"][i],
                  "corso": infos["corso"][i],
                  "voto": infos["voto"][i]}
        new_list.append(record)
    return new_list 


infos = {
    "nome": ["Lisa", "Gianna", "Lucia"],
    "corso": ["Matematica", "Geometria", "Storia"],
    "voto": [18, 23, 28]
}

print(diz_converti(infos))
print()


def converti_dict(informazioni: dict[str, list[str|int]]) -> list[dict]:
    return [{"nome":nome, "corso": corso, "voto": voto} for nome, corso, voto in zip(informazioni["nome"], informazioni["corso"], informazioni["voto"])]


informazioni = {"nome": ["Pippo", "Lisa", "Nico"],
                "corso": ["Python", "Children", "React"],
                "voto": [24, 28, 27]
                }

print(converti_dict(informazioni))



def converti(dizion: dict[str, list[str, int]]) -> list[dict]:
    lista_nuova = []
    n = len(dizion("nome"))
    for i in range(n):
        record = {}
        for chiave in dizion:
            record[chiave] = record[chiave][i]
        lista_nuova.append(record)
    return lista_nuova



def converti(diz: dict[str, list[str, int]]) -> list[dict]:
    lista_nuova = []
    n = len(diz("nome"))
    for i in range(n):
        record = {"nome": dizion["nome"][i],
                  "corso": dizion["corso"][i],
                  "voto": dizion["voto"][i]
                  }
        lista_nuova.append(record)
    return lista_nuova 


def converti(dizio: dict[str, list[str, int]]) -> list[dict]:
    return [{"nome": nome, "corso": corso, "voto": voto} for nome, corso, voto in zip(dizio["nome"], dizio["corso"], dizio["voto"])]




dizion = {"nome": ["Pippo", "Lisa", "Nico"],
          "corso": ["Python", "Children", "React"],
          "voto": [24, 28, 27]
          }