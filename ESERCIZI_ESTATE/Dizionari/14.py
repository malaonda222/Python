'''Scrivi una funzione media_voti_sopra che, data una lista di studenti 
(ognuno rappresentato da un dizionario con nome e lista di voti numerici), 
e una soglia numerica, ritorni un dizionario che associa a ogni studente la 
media dei voti, superiore o uguale a quella soglia.
 
Input esempio:
studenti = [
    {"nome": "Anna", "voti": [15, 18, 22, 10]},
    {"nome": "Luca", "voti": [20, 17, 19, 13]},
    {"nome": "Sara", "voti": [12, 16, 14]},
]'''

def media_voti_sopra(studenti: list[dict[str, list[int]]], soglia: int) -> dict[str, float]:
    new_dict = {}
    for studente in studenti:
        contatore = 0
        somma_voti = 0
        for voto in studente["voti"]:
            if voto >= soglia:
                contatore += 1
                somma_voti += voto
        if contatore > 0:
            media = (somma_voti/contatore)
        else:
            media = 0.0 
        new_dict[studente["nome"]] = media 
    return new_dict

def media_voti_sopra2(studenti: list[dict[str, list[int]]], soglia: int) -> dict[str, float]:
    new_dict = {}
    for studente in studenti:
        voti_validi = [voto for voto in studente["voti"] if voto >= soglia]
        if voti_validi:
            media = sum(voti_validi)/len(voti_validi)
        else:
            media = 0.0
        new_dict[studente["nome"]] = media
    return new_dict
        

studenti = [
    {"nome": "Anna", "voti": [15, 18, 22, 10]},
    {"nome": "Luca", "voti": [20, 17, 19, 13]},
    {"nome": "Sara", "voti": [12, 16, 14]},
]

print(media_voti_sopra(studenti, 17))
print(media_voti_sopra2(studenti, 19))