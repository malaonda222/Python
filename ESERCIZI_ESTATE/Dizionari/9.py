'''Immagina di avere un dizionario con il punteggio di diversi studenti 
in un esame, dove le chiavi sono i nomi degli studenti e i valori sono i 
loro punteggi. Scrivi una funzione che calcoli la media dei punteggi.'''

def calcola_media(dizionario: dict[str, int]) -> int:
    somma_punteggio = 0
    contatore = 0
    for punteggio in dizionario.values():
        somma_punteggio += punteggio
        contatore += 1
    if contatore == 0:
        return 0
    return f"La media dei punteggi è: {somma_punteggio/contatore:.2f}"


dizionario: dict = {
    {"Lisa": 10},
    {"Gianni": 13},
    {"Clara": 9}
    }

print(calcola_media(dizionario))


def calcola_media2(dizionario: dict[str, int]) -> float:
    somma_punt = sum(dizionario.values())
    numero_studenti = len(dizionario)
    if numero_studenti == 0:
        return 0
    return f"{somma_punt/numero_studenti:.2f}"



