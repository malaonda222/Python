'''
Traccia:
Scrivi una funzione studente_migliore(studenti: dict[str, int]) -> tuple[str, int] che, 
dato un dizionario studenti con nome → voto, ritorni una tupla contenente il nome e il 
voto dello studente con il punteggio più alto.
 
Suggerimento:
Puoi usare un ciclo per confrontare i voti, oppure la funzione max() con una chiave.'''

def studente_migliore(studenti: dict[str, int]) -> tuple[str, int]:
    voto_massimo = max(studenti.values())
    for nome, voto in studenti.items():
        if voto == voto_massimo:
            return (nome, voto)


studenti = {
    "Marco": 25,
    "Luca": 18,
    "Anna": 30,
    "Giulia": 27,
    "Paolo": 22
}

print(studente_migliore(studenti))