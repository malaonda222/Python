'''Scrivi una funzione media_voti_maggiorenni(studenti) che calcoli e ritorni la media dei voti degli 
studenti con età ≥ 18, utilizzando list comprehension per estrarre i voti.'''

def media_voti_maggiorenni(studenti: dict[str, dict[str, int]]) -> float:
    voti_maggiorenni = []
    for dati in studenti.values():
        voto = dati["voto"]
        eta = dati["eta"]
        if eta >= 18:
            voti_maggiorenni.append(voto)
    media = sum(voti_maggiorenni)/len(voti_maggiorenni)
    return f"Media: {media:.2f}" 

def media_voti_maggiorenni2(studenti: dict[str, dict[str, int]]) -> float:
    voti_maggiorenni = [dati["voto"] for dati in studenti.values() if dati["eta"] >= 18]
    return f"Media: {sum(voti_maggiorenni)/len(voti_maggiorenni):.2f}"



studenti = {
    "Marco": {"eta": 20, "voto": 28},
    "Luca": {"eta": 22, "voto": 18},
    "Anna": {"eta": 19, "voto": 30},
    "Mario": {"eta": 25, "voto": 27},
    "Carlotta": {"eta": 20, "voto": 26},
    "Giuseppe": {"eta": 18, "voto": 20},
}

print(media_voti_maggiorenni(studenti))
print(media_voti_maggiorenni2(studenti))