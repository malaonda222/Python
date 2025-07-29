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