'''Data una lista di dizionari con nome e voto, restituisci solo gli 
studenti con voto ≥ 18.'''

def studenti_promossi(studenti: list[dict[str, list[int]]]) -> list[str]:
    promossi = []
    for studente in studenti:
        for voto in studente["voti"]:
            if voto >= 18:
                promossi.append(studente["nome"])
                break
    return promossi
    
def studenti_promossi2(studenti: list[dict[str, list[int]]]) -> list[str]:
    return [studente["nome"] for studente in studenti if all(voto >= 18 for voto in studente["voti"])]



studenti = [
    {"nome": "Anna", "voti": [15, 18, 22, 10]},
    {"nome": "Luca", "voti": [20, 17, 19, 13]},
    {"nome": "Sara", "voti": [22, 26, 19]},
]

print(studenti_promossi(studenti))
print(studenti_promossi2(studenti))
