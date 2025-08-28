'''
Traccia:
Hai una lista di studenti, ciascuno rappresentato da un dizionario con:
"nome" → nome dello studente
"materie" → dizionario in cui le chiavi sono materie e i valori sono liste di voti
 
Scrivi una funzione che restituisca un dizionario in cui:
ogni chiave è il nome dello studente e il valore è un dizionario con il voto più basso di ogni materia
 
Esempio di input:
 
studenti = [
    {"nome": "Marco", "materie": {"matematica": [24, 18, 30], "storia": [18, 20]}},
    {"nome": "Giulia", "materie": {"matematica": [21, 22], "storia": [20, 19]}},
    {"nome": "Elena", "materie": {"matematica": [26, 25], "storia": [17, 21]}}
]'''

def voto_minimo_per_studente(studenti: list[dict]) -> dict[str, dict[str, int]]:
    nuovo_dizionario = {}
    for studente in studenti:
        nome= studente["nome"]
        materie = studente["materie"]
        voto_minimo_materie = {}
        for materia, voti in materie.items():
            voto_minimo_materie[materia] = min(voti)
        nuovo_dizionario[nome] = voto_minimo_materie

    return nuovo_dizionario
            






studenti = [
    {"nome": "Marco", "materie": {"matematica": [24, 18, 30], "storia": [18, 20]}},
    {"nome": "Giulia", "materie": {"matematica": [21, 22], "storia": [20, 19]}},
    {"nome": "Elena", "materie": {"matematica": [26, 25], "storia": [17, 21]}}
]