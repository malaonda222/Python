'''
Traccia:
Data una struttura tipo:
 
studenti = {
    "Marco": {"eta": 20, "voto": 28},
    "Luca": {"eta": 22, "voto": 18},
    "Anna": {"eta": 19, "voto": 30},
    "Mario": {"eta": 25, "voto": 27},
    "Carlotta": {"eta": 20, "voto": 26},
    "Giuseppe": {"eta": 18, "voto": 20},
}
 
Scrivi una funzione studenti_promossi(studenti) che ritorni una lista con 
i nomi degli studenti che hanno almeno 21 anni e che hanno voto ≥ 18, usando dictionary/list comprehension.'''

def studenti_promossi(studenti: dict[str, dict[str, int]]) -> list[str]:
    lista_studenti = []
    for nome, dati in studenti.items(): 
        eta = dati["eta"]
        voto = dati["voto"]
        if eta >= 21 and voto >= 18:
            lista_studenti.append(nome)
    return lista_studenti

def studenti_promossi2(studenti: dict[str, dict[str, int]]) -> list[str]:
    return [nome for nome, dati in studenti.items() if dati["eta"] >= 21 and dati["voto"] >= 18]


studenti = {
    "Marco": {"eta": 20, "voto": 28},
    "Luca": {"eta": 22, "voto": 18},
    "Anna": {"eta": 19, "voto": 30},
    "Mario": {"eta": 25, "voto": 27},
    "Carlotta": {"eta": 20, "voto": 26},
    "Giuseppe": {"eta": 18, "voto": 20},
}

print(studenti_promossi(studenti))
print(studenti_promossi2(studenti))