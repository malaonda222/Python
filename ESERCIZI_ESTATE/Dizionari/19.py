'''Esercizio: voto_massimo_sotto

Scrivi una funzione chiamata voto_massimo_sotto che, data una lista di studenti (ognuno rappresentato da un dizionario con nome e lista di voti numerici) 
e una soglia numerica, ritorni un dizionario che associa a ogni studente il voto massimo tra quelli inferiori alla soglia.

Se uno studente non ha voti inferiori alla soglia, il voto massimo sarà None.
Esempio di input:

studenti = [
    {"nome": "Marco", "voti": [10, 25, 30, 18]},
    {"nome": "Giulia", "voti": [28, 16, 12]},
    {"nome": "Elena", "voti": [24, 26]},
]

soglia = 20'''


def voto_massimo_sotto(studenti: list[dict[str, list[int]]], soglia: int) -> dict[str, int]:
    new_dict = {}
    for studente in studenti:
        voti_inferiori_soglia = []
        for voto in studente["voti"]:
            if voto < soglia:
                voti_inferiori_soglia.append(voto)
        if voti_inferiori_soglia:
            massimo = voti_inferiori_soglia[0]
            for voto in voti_inferiori_soglia:
                if voto > massimo:
                    massimo = voto 
            new_dict[studente["nome"]] = massimo 
        else:
            new_dict[studente["nome"]] = None
    return new_dict



def voto_massimo_sotto2(studenti: list[dict[str, list[int]]], soglia: int) -> dict[str, int]:
    new_dict = {}
    for studente in studenti:
        nome = studente["nome"]
        voti = studente["voti"]
        voti_inferiori = (voto for voto in voti if voto < soglia)
        if voti_inferiori:
            massimo = max(voti_inferiori)
            new_dict[nome] = massimo
        else:
            new_dict[nome] = None 
    return new_dict



studenti = [
    {"nome": "Marco", "voti": [10, 25, 30, 18]},
    {"nome": "Giulia", "voti": [28, 16, 12]},
    {"nome": "Elena", "voti": [24, 26]},
]

print(voto_massimo_sotto(studenti, 20))
