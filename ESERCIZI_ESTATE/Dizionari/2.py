'''Hai una lista di dizionari, ognuno rappresenta uno studente e i suoi voti.
Scrivi una funzione almeno_una_sufficienza(studenti: list[dict]) -> list[str]
che restituisce una lista con i nomi degli studenti che hanno almeno un voto superiore a 18.
 
studenti = [
    {"nome": "Anna", "voti": {"matematica": 25, "storia": 30, "inglese": 17}},
    {"nome": "Luca", "voti": {"matematica": 22, "storia": 21, "inglese": 26}},
    {"nome": "Marco", "voti": {"matematica": 16, "storia": 20, "inglese": 19}},
    {"nome": "Giulia", "voti": {"matematica": 28, "storia": 29, "inglese": 30}},
]'''

def almeno_una_sufficienza(studenti: list[dict]) -> list[str]:
    lista_studenti: list = []
    for studente in studenti:
        voti_stud = studente["voti"]
        for voto in voti_stud.values():
            if voto > 18:
                lista_studenti.append(studente["nome"])
                break 
    return lista_studenti

studenti = [
    {"nome": "Anna", "voti": {"matematica": 25, "storia": 30, "inglese": 17}},
    {"nome": "Luca", "voti": {"matematica": 22, "storia": 21, "inglese": 26}},
    {"nome": "Marco", "voti": {"matematica": 16, "storia": 20, "inglese": 19}},
    {"nome": "Giulia", "voti": {"matematica": 28, "storia": 29, "inglese": 30}},
]
print(almeno_una_sufficienza(studenti))

def almeno_una_sufficienza(studenti: list[dict]) -> list[str]:
    lista_stud: list = []
    for studente in studenti:
        voti_studente = studente["voti"]
        if any(voto > 18 for voto in voti_studente.values()):
            lista_stud.append(studente["nome"])
    return lista_stud