'''Traccia:
Scrivi una funzione che prende un dizionario con chiavi stringa e valori 
qualsiasi e restituisce una lista di tuple ordinate in base alla lunghezza delle chiavi in ordine crescente.
 
dati = {
    "Anna": 24,
    "Luca": 30,
    "Martina": 21,
    "Al": 40
}
 
# Ordinato per lunghezza chiave (dal più corto al più lungo):
# [('Al', 40), ('Anna', 24), ('Luca', 30), ('Martina', 21)]'''

def converti_dizionario(dizionario: dict[str, int]) -> list[tuple]:
    lista_tuple = list(dizionario.items())
    n = len(lista_tuple)
    for i in range(n):
        for j in range(n-i-1):
            if len(lista_tuple[j][0])>len(lista_tuple[j+1][0]):
                lista_tuple[j], lista_tuple[j+1] = lista_tuple[j+1], lista_tuple[j]
    return lista_tuple

print(converti_dizionario({
    "Anna": 24,
    "Luca": 30,
    "Martina": 21,
    "Al": 40
}))
