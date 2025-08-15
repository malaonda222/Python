'''Nome dell’esercizio: peggior_voto_per_materia
 
Traccia:
Hai un elenco di studenti con un dizionario di materie e relativi voti.
Restituisci un nuovo dizionario dove ogni materia è una chiave e il valore 
è una tupla (nome_studente, voto) corrispondente al voto più basso per quella materia.
 
Input:
studenti = [
    {"nome": "Marco", "materie": {"matematica": 24, "storia": 18}},
    {"nome": "Giulia", "materie": {"matematica": 21, "storia": 20}},
    {"nome": "Elena", "materie": {"matematica": 26, "storia": 17}}
]'''


def peggior_voto_per_materia(studenti: list[str, dict[str, int]]) -> dict[tuple[str, int]]:
    new_dict = {}
    for studente in studenti:
        for materia, voto in studente["materie"].items():
            if materia not in new_dict:
                new_dict[materia] = (studente["nome"], voto)
            else:
                if voto < new_dict[materia][1]:
                    new_dict[materia] = (studente["nome"], voto)
    return new_dict

studenti = [
    {"nome": "Marco", "materie": {"matematica": 24, "storia": 18}},
    {"nome": "Giulia", "materie": {"matematica": 21, "storia": 20}},
    {"nome": "Elena", "materie": {"matematica": 26, "storia": 17}}
]

print(peggior_voto_per_materia(studenti))



