'''Scrivi una funzione chiamata media_voti_sopra che, data una lista di studenti (ognuno rappresentato da un dizionario con nome e lista di voti numerici) 
e una soglia numerica, ritorni un dizionario che associa a ogni studente la media dei voti superiori o uguali a quella soglia.
Se uno studente non ha voti che soddisfano la condizione, la media sarà 0.
Esempio di input:
 
studenti = [
    {"nome": "Marco", "voti": [10, 25, 30, 18]},
    {"nome": "Giulia", "voti": [28, 16, 12]},
    {"nome": "Elena", "voti": [14, 15]},
]
 
soglia = 20'''

def media_voti_sopra(lista_studenti: list[dict[str, list[int]]], soglia: int) -> dict[str, int]:
    new_dict = {}
    for studente in lista_studenti:
        voti_validi = [voto for voto in studente["voti"] if voto >= soglia]
        if not voti_validi:
            media = 0.0
        else:
            media = sum(voti_validi)/len(voti_validi)
        new_dict[studente["nome"]] = media  
    return new_dict

studenti = [
    {"nome": "Marco", "voti": [10, 25, 30, 18]},
    {"nome": "Giulia", "voti": [28, 16, 12]},
    {"nome": "Elena", "voti": [14, 15]},
]
print(media_voti_sopra(studenti, 15))