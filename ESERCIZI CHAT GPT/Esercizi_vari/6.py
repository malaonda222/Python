'''Scrivi una funzione che restituisce una lista di dizionari in cui ogni 
dizionario rappresenta una persona.'''

def converti(dati: dict[str, list[str|int]]) -> list[dict]:
    lista_nuova = []
    lunghezza = len(next(iter(dati.values())))
    for i in range(lunghezza):
        record = {}
        for chiave in dati:
            record[chiave] = dati[chiave][i]
        lista_nuova.append(record)
    return lista_nuova

dati = {
    "nome": ["Giulia", "Davide", "Sara"],
    "età": [22, 24, 21]
}
print(converti(dati))



def converti_lista(dizionario: dict[str, list[str|int]]) -> list[dict]:
    return [{"nome": nome, "eta": eta} for nome, eta in zip(dizionario["nome"], dizionario["eta"])]


dizionario = {
    "nome": ["Antonio", "Elena", "Silvia"],
    "eta": [22, 24, 21]
}

print(converti_lista(dizionario))



def convert_list(dizio: dict[str, list[str|int]]) -> list[dict]:
    lista_nuova = []
    lunghezza = len(dizio["nome"])
    for i in range(lunghezza):
        record = {}
        for chiave in dizio:
            record[chiave] = dizio[chiave][i]
        lista_nuova.append(record)
    return lista_nuova