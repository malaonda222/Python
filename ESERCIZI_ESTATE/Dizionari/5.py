'''Scrivi una funzione che prende un dizionario con chiavi stringa e valori 
qualsiasi e restituisce una lista di tuple ordinate in base alla lunghezza delle chiavi 
in ordine crescente.
 
dati = {
    "Anna": 24,
    "Luca": 30,
    "Martina": 21,
    "Al": 40
}
 
# Ordinato per lunghezza chiave (dal più corto al più lungo):
# [('Al', 40), ('Anna', 24), ('Luca', 30), ('Martina', 21)]'''

def tupla_ordinata(dati: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(dati.items(), key=lambda item: len(item[0]), reverse=False)

print(tupla_ordinata(dati={
    "Anna": 24,
    "Luca": 30,
    "Martina": 21,
    "Al": 40
}))

def tupla_ordinata(dati: dict[str, int]) -> list[tuple[str, int]]:
    lista = list(dati.items())
    for i in range(len(lista)):
        min_index = i
        for j in range(i + 1, len(lista)):
            if len(lista[j][0]) < len(lista[min_index][0]):
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]

    return lista