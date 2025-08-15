'''Scrivi una funzione chiamata voto_minimo_sopra che, data una lista di studenti (ognuno rappresentato da un dizionario con nome e una 
lista di voti numerici) e una soglia numerica, ritorni un dizionario che associa a ogni studente il voto minimo tra quelli superiori o 
uguali alla soglia.

Se uno studente non ha voti superiori o uguali alla soglia, il valore associato sarà None.
studenti = [
    {"nome": "Luca", "voti": [22, 19, 30]},
    {"nome": "Anna", "voti": [15, 18, 17]},
    {"nome": "Sara", "voti": [20, 21, 19]},
]
'''

def voto_minimo_sopra(list_students: list[dict[str, list[int]]], soglia: int) -> dict[str, int]:
    new_dizionario = {}
    for studente in list_students:
        nome = studente["nome"]
        voti = studente["voti"]
        lista_superiori = [voto for voto in voti if voto >= soglia]
        if lista_superiori:
            new_dizionario[nome] = min(lista_superiori)
        else:
            new_dizionario[nome] = None 
    return new_dizionario

studenti = [
    {"nome": "Luca", "voti": [22, 19, 30]},
    {"nome": "Anna", "voti": [15, 18, 17]},
    {"nome": "Sara", "voti": [20, 21, 19]},
]
print(voto_minimo_sopra(studenti, 18))