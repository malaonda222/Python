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

def modifica_dizionario(dizionario: dict[str, int]) -> list[tuple]:
    lista_tuple = []
    for key, value in dizionario.items():
        lista_tuple.append((key, value))
    
    n = len(lista_tuple)
    for i in range(n):
        for j in range(n-i-1):
            if lista_tuple[j][1] < lista_tuple[j+1][1]:
                lista_tuple[j], lista_tuple[j+1] = lista_tuple[j+1], lista_tuple[j]

    return lista_tuple


