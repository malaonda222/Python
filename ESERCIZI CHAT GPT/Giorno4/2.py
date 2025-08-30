'''Con la stessa struttura dati, scrivi una funzione studenti_minorenni(studenti) 
che ritorni una lista dei nomi degli studenti con età < 20.'''

def studenti_minorenni(studenti: dict[str, dict[str, int]]) -> list[str]:
    lista_minorenni = []
    for nome, dati in studenti.items():
        eta = dati["eta"]
        if eta < 20:
            lista_minorenni.append(nome)
    return lista_minorenni

def studenti_minorenni2(studenti: dict[str, dict[str, int]]) -> list[str]:
    return [nome for nome, dati in studenti.items() if dati["eta"] < 20]
            


studenti = {
    "Marco": {"eta": 20, "voto": 28},
    "Luca": {"eta": 22, "voto": 18},
    "Anna": {"eta": 19, "voto": 30},
    "Mario": {"eta": 25, "voto": 27},
    "Carlotta": {"eta": 20, "voto": 26},
    "Giuseppe": {"eta": 18, "voto": 20},
}

print(studenti_minorenni(studenti))
print(studenti_minorenni2(studenti))
