'''Scrivi una funzione che prenda in input un dizionario con chiavi stringa e valori numerici, 
e restituisca una lista di tuple ordinate in base ai valori, dal più alto al più basso.
 
Esempio:
 
dati = {
    "Anna": 24,
    "Luca": 30,
    "Marta": 21
}
Output desiderato:
[('Luca', 30), ('Anna', 24), ('Marta', 21)]'''

def tupla_ordinata(dati: dict[str, int]) -> list[tuple[str, int]]:
    valori_ordinati = sorted(dati.items(), key=lambda item: item[1], reverse=True)
    return valori_ordinati

print(tupla_ordinata(dati = {
    "Anna": 24,
    "Luca": 30,
    "Marta": 21
}))

def tupla_crescente(dati: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(dati.items(), key=lambda item: item[1], reverse=False)

print(tupla_crescente(dati = {
    "Anna": 24,
    "Luca": 30,
    "Marta": 21
}))
        