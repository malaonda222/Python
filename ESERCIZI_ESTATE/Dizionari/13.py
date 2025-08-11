'''Scrivi una funzione somma_voti_sopra che, data una lista di studenti 
(ognuno rappresentato da un dizionario con nome e lista di voti numerici), 
e una soglia numerica, ritorni un dizionario che associa a ogni studente la 
somma dei voti superiori o uguali a quella soglia.
 
Input esempio:
studenti = [
    {"nome": "Anna", "voti": [15, 18, 22, 10]},
    {"nome": "Luca", "voti": [20, 17, 19, 13]},
    {"nome": "Sara", "voti": [12, 16, 14]},
]'''

def somma_voti_sopra(studenti: list[dict[str, list[int]]], soglia: int) -> dict[str, int]:
    new_dict = {}
    for studente in studenti:
        somma_voti = 0
        for voto in studente["voti"]:
            if voto >= soglia:
                somma_voti += voto 
        new_dict[studente["nome"]] = somma_voti
    return new_dict

def somma_voti_sopra2(studenti: list[dict[str, list[int]]], soglia: int) -> dict[str, int]:
    new_dict = {}
    for studente in studenti:
        somma_voti = sum(voto for voto in studente["voti"] if voto >= soglia)
        new_dict[studente["nome"]] = somma_voti
    return new_dict



studenti = [
    {"nome": "Anna", "voti": [15, 18, 22, 10]},
    {"nome": "Luca", "voti": [20, 17, 19, 13]},
    {"nome": "Sara", "voti": [12, 16, 14]}
]
print(somma_voti_sopra(studenti, 17))
print(somma_voti_sopra2(studenti, 17))