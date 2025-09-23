'''
Esercizio - 01
Nome dell’esercizio: ordina_per_lunghezza_chiave
Traccia:
Scrivi una funzione che prende un dizionario con chiavi stringa e valori 
qualsiasi e restituisce una lista di tuple ordinate in base alla lunghezza delle chiavi in ordine crescente.
'''

def ordina_per_lunghezza_chiave(my_dict: dict[str, int]) -> list[tuple]:
    lista_tuple = list(my_dict.items())
    n = len(lista_tuple)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(lista_tuple[j][0]) > len(lista_tuple[j+1][0]):
                lista_tuple[j], lista_tuple[j+1] = lista_tuple[j+1], lista_tuple[j]
    return lista_tuple


def ordina_per_lunghezza_chiave1(my_dict: dict[str, int]) -> list[tuple]:
    return sorted(my_dict.items(), key=lambda x: len(x[0]))


def ordina_per_lunghezza_chiave2(my_dict: dict[str, int]) -> list[tuple]:
    return [elemento for elemento in sorted(my_dict.items(), key=lambda elemento: len(elemento[0]))]




dati = {
    "Anna": 24,
    "Luca": 30,
    "Martina": 21,
    "Al": 40
}
print(ordina_per_lunghezza_chiave(dati))
print(ordina_per_lunghezza_chiave1(dati))
print(ordina_per_lunghezza_chiave2(dati))
