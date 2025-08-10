'''Hai una lista di dizionari, ognuno rappresenta uno studente e i suoi voti.
Scrivi una funzione ha_insufficienze(studenti: list[dict]) -> list[str]
che restituisce una lista con i nomi degli studenti che hanno almeno un voto inferiore a 18.
 
studenti = [
    {"nome": "Anna", "voti": {"matematica": 25, "storia": 30, "inglese": 17}},
    {"nome": "Luca", "voti": {"matematica": 22, "storia": 21, "inglese": 26}},
    {"nome": "Marco", "voti": {"matematica": 16, "storia": 20, "inglese": 19}},
    {"nome": "Giulia", "voti": {"matematica": 28, "storia": 29, "inglese": 30}},
]'''

def ha_insufficienza(studenti: list[dict]) -> list[dict]:
    lista_studenti_voto_meno_di_18 = []
    for studente in studenti:
        voti_studente = studente["voti"]
        for voto in voti_studente.values():
            if voto < 18:   
                lista_studenti_voto_meno_di_18.append(studente["nome"])
                break
    return lista_studenti_voto_meno_di_18

studenti = [
    {"nome": "Anna", "voti": {"matematica": 25, "storia": 30, "inglese": 17}},
    {"nome": "Luca", "voti": {"matematica": 22, "storia": 21, "inglese": 26}},
    {"nome": "Marco", "voti": {"matematica": 16, "storia": 20, "inglese": 19}},
    {"nome": "Giulia", "voti": {"matematica": 28, "storia": 29, "inglese": 30}},
]
print(ha_insufficienza(studenti))


def ha_insufficienza2(studenti: list[dict]) -> list[dict]:
    lista_insufficienti = []
    for studente in studenti:
        voto_stud = studente["voti"]
        if any(voto < 18 for voto in voto_stud.values()):
            lista_insufficienti.append(studente["nome"])
    return lista_insufficienti
    
studenti = [
    {"nome": "Anna", "voti": {"matematica": 25, "storia": 30, "inglese": 17}},
    {"nome": "Luca", "voti": {"matematica": 22, "storia": 21, "inglese": 26}},
    {"nome": "Marco", "voti": {"matematica": 16, "storia": 20, "inglese": 19}},
    {"nome": "Giulia", "voti": {"matematica": 28, "storia": 29, "inglese": 30}},
]
print(ha_insufficienza2(studenti))