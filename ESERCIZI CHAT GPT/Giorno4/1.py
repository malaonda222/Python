'''Scrivi una funzione studenti_eccellenti(studenti) che ritorna un dizionario 
con solo gli studenti che hanno preso voto ≥ 28, usando dictionary comprehension.'''

def studenti_eccellenti(studenti: dict[str, dict[str, int]]) -> dict[str, int]:
    nuovo_dizionario = {}
    for nome, dati in studenti.items():
        voto = dati["voto"]
        if voto >= 28:
            nuovo_dizionario[nome] = voto 
    return nuovo_dizionario

def studenti_eccellenti2(studenti: dict[str, dict[str, int]]) -> dict[str, int]:
    return {nome: dati["voto"] for nome, dati in studenti.items() if dati["voto"] >= 28}



studenti = {
    "Marco": {"eta": 20, "voto": 28},
    "Luca": {"eta": 22, "voto": 18},
    "Anna": {"eta": 19, "voto": 30},
    "Mario": {"eta": 25, "voto": 27},
    "Carlotta": {"eta": 20, "voto": 26},
    "Giuseppe": {"eta": 18, "voto": 20},
}
print(studenti_eccellenti(studenti))
print(studenti_eccellenti2(studenti))
