'''Nome dell’esercizio: peggior_voto_per_materia
 
Traccia:
Hai un elenco di studenti con un dizionario di materie e una lista con i suoi relativi voti.
Restituisci un nuovo dizionario dove ogni materia è una chiave e il valore 
è una tupla (nome_studente, voto) corrispondente al voto più basso (tra tutti quelli che si trovano nella lista) 
per quella materia.
 
Input:
studenti = [
    {"nome": "Marco", "materie": {"matematica": [24, 18, 30], "storia": [18, 20]}},
    {"nome": "Giulia", "materie": {"matematica": [21, 22], "storia": [20, 19]}},
    {"nome": "Elena", "materie": {"matematica": [26, 25], "storia": [17, 21]}}
]
 
Esempio output atteso: un dizionario del tipo {"matematica": ("Marco", 18).
'''


def peggior_voto_per_materia(studenti: list[dict[str, dict[str, list[int]]]]) -> dict[tuple[str, int]]:
    new_dict = {}
    for studente in studenti:
        for materia, voti in studente["materie"].items():
            voto_minimo = min(voti)
            if materia not in new_dict:
                new_dict[materia] = (studente["nome"], voto_minimo) 
            else:
                if voto_minimo < new_dict[materia][1]:
                    new_dict[materia] = (studente["nome"], voto_minimo)
    return new_dict

studenti = [
    {"nome": "Marco", "materie": {"matematica": [24, 18, 30], "storia": [18, 20]}},
    {"nome": "Giulia", "materie": {"matematica": [21, 22], "storia": [20, 19]}},
    {"nome": "Elena", "materie": {"matematica": [26, 25], "storia": [17, 21]}}
]

print(peggior_voto_per_materia(studenti))