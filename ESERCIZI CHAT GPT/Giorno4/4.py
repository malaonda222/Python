'''Uno studente è promosso se ha preso voto ≥ 18. 
Scrivi una funzione eta_media_promossi(studenti) che calcoli e 
ritorni l’età media degli studenti promossi.'''

def eta_media_promossi(studenti: dict[str, dict[str, int]]) -> float:
    lista_eta = []
    for dati in studenti.values():
        eta = dati["eta"]
        voto = dati["voto"]
        if voto >= 18:
            lista_eta.append(eta)
    eta_media = sum(lista_eta) / len(lista_eta)
    return f"Età media: {eta_media:.2f}"

def eta_media_promossi2(studenti: dict[str, dict[str, int]]) -> float:
    eta_superiore = [dati["eta"] for dati in studenti.values() if dati["voto"] >= 18]
    return f"Media: {sum(eta_superiore) / len(eta_superiore):.2f}"

studenti = {
    "Marco": {"eta": 20, "voto": 28},
    "Luca": {"eta": 22, "voto": 18},
    "Anna": {"eta": 19, "voto": 30},
    "Mario": {"eta": 25, "voto": 27},
    "Carlotta": {"eta": 20, "voto": 26},
    "Giuseppe": {"eta": 18, "voto": 20},
}
print(eta_media_promossi(studenti))
print(eta_media_promossi2(studenti))
