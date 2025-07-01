# Doppio ordinamento 

studenti = [
    {"nome": "Anna", "media": 28},
    {"nome": "Luca", "media": 25},
    {"nome": "Marco", "media": 30}
]

lista_decrescente = list(sorted(studenti, key=lambda studente: studente["media"], reverse = True))
print(lista_decrescente)



def media_studenti(studente):
    return studente["media"]
 
studenti = [
    {"nome": "Anna", "media": 28},
    {"nome": "Luca", "media": 25},
    {"nome": "Marco", "media": 30}
]
 
studenti_ordinati = sorted(studenti, key=media_studenti, reverse=True)
print(studenti_ordinati)