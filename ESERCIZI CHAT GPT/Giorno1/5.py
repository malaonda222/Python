'''Traccia:
Scrivi una funzione studenti_promossi(studenti: dict[str, int], soglia: int) -> dict[str, int] che, 
dato un dizionario studenti con nome → voto e una soglia, ritorni un nuovo dizionario con solo gli 
studenti che hanno un voto maggiore o uguale alla soglia.'''


def studenti_promossi(studenti: dict[str, int], soglia: int) -> dict[str, int]:
    new_dict = {}
    for nome, voto in studenti.items():
        if voto >= soglia:
            new_dict[nome] = voto
    return new_dict


def studenti_promossi2(studenti: dict[str, int], soglia: int) -> dict[str, int]:
    return {nome: voto for nome, voto in studenti.items() if voto >= soglia}


studenti = {
    "Marco": 28,
    "Luca": 18,
    "Anna": 30,
    "Giulia": 22,
    "Paolo": 15
}

print(studenti_promossi(studenti, 20))
print(studenti_promossi2(studenti, 20))
