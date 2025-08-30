'''Scrivi una funzione voti_ordinati(studenti) che ritorni una lista 
di voti ordinati in ordine decrescente, usando list comprehension 
e la funzione sorted().'''

def voti_ordinati(studenti: dict[str, dict[str, int]]) -> list[int]:
    return sorted([dati["voto"] for dati in studenti.values()], reverse = True)


studenti = {
    "Marco": {"eta": 20, "voto": 28},
    "Luca": {"eta": 22, "voto": 18},
    "Anna": {"eta": 19, "voto": 30},
    "Mario": {"eta": 25, "voto": 27},
    "Carlotta": {"eta": 20, "voto": 26},
    "Giuseppe": {"eta": 18, "voto": 20},
}
print(voti_ordinati(studenti))