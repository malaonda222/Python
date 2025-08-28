'''Tema: Dizionari
Obiettivo: Contare e costruire mapping.
 
Nome: Frequenza valori in lista
 
Traccia:
Scrivi una funzione conteggio_elementi(lista) che ritorni un dizionario 
in cui le chiavi sono gli elementi della lista e i valori quante volte compaiono.
 
lista = ["mela", "banana", "mela", "pera", "banana", "mela"]
'''

def conteggio_elementi(lista: list[str]) -> dict[str, int]:
    nuovo_dizionario: dict = {}
    if not lista:
        return "La lista è vuota"
    for element in lista:
        if element not in nuovo_dizionario:
            nuovo_dizionario[element] = 1 
        else:
            nuovo_dizionario[element] += 1 
    return nuovo_dizionario

lista = ["mela", "banana", "mela", "pera", "banana", "mela"]
print(conteggio_elementi(lista))