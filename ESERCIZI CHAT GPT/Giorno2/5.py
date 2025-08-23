'''Scrivi una funzione che, data una lista di parole (stringhe), ritorni un dizionario in cui:
Le chiavi sono le lettere iniziali maiuscole di ciascuna parola (es. "A", "B", ecc.).
I valori sono liste di parole che iniziano con quella lettera, indipendentemente dal fatto che 
siano scritte in minuscolo o maiuscolo.'''

def raggruppa_per_iniziale(parole: list[str]) -> dict[str, list[str]]:
    new_dizionario = {}
    for parola in parole:
        prima_lettera = parola[0].upper()
        if prima_lettera not in new_dizionario:
            new_dizionario[prima_lettera] = []
        new_dizionario[prima_lettera].append(parola)       
    return new_dizionario

parole = ["albero", "Ape", "banana", "Barca", "asino", "ciliegia", "Cane"]
print(raggruppa_per_iniziale(parole))

