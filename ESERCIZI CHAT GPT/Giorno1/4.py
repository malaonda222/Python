'''"Nome dell’esercizio: Conteggio delle vocali
Traccia:
Scrivi una funzione conteggia_vocali(parole: list[str]) -> dict[str, int] che, 
data una lista di parole, ritorni un dizionario in cui le chiavi sono le vocali 
(a, e, i, o, u) e i valori sono il numero di volte che ciascuna vocale compare in tutte le parole della lista.
Se una vocale non compare mai, non deve comparire nel dizionario."'''

def conteggia_vocali(parole: list[str]) -> dict[str, int]:
    vocali: str = "aeiou"
    dizionario: dict = {}
    for parola in parole:
        for lettera in parola.lower():
            if lettera in vocali:
                if lettera not in dizionario:
                    dizionario[lettera] = 1
                else:
                    dizionario[lettera] += 1
    return dizionario


parole = ["ioplsfjhgbcm", "jhdhddkelefaaaeaalossuuiii"]
print(conteggia_vocali(parole))