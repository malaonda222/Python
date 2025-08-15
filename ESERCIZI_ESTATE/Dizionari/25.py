'''Tema: Liste di dizionari - Filtraggio e aggregazione
Obiettivo: Trovare gli studenti che hanno almeno un voto sopra 
una soglia e calcolare per ciascuno la media dei loro voti.
 
Nome dell’esercizio: studenti_media_se_hanno_voto_alto
 
Traccia:
Data una lista di studenti con i loro voti, restituisci un dizionario 
dove la chiave è il nome dello studente e il valore è la sua media, 
solo se ha almeno un voto è maggiore o uguale alla soglia data.
 
 
Esempio di input:
studenti = [
    {"nome": "Marco", "voti": [10, 25, 30, 18]},
    {"nome": "Giulia", "voti": [18, 16, 19]},
    {"nome": "Elena", "voti": [24, 26]},
]
soglia = 20'''


def studenti_media_se_hanno_voto_alto(studenti: list[dict[str, int]], soglia: int) -> dict[str, float]:
    new_dict = {}
    for studente in studenti:
        voti_superiori = []
        for voto in studente["voti"]:
            if voto >= 18:
                voti_superiori.append(voto)
        if not voti_superiori:
            new_dict[studente["nome"]] = None 
        else:
            media = sum(voti_superiori)/len(voti_superiori)
            new_dict[studente["nome"]] = media 
    return new_dict


studenti = [
    {"nome": "Marco", "voti": [10, 15, 16, 17]},
    {"nome": "Giulia", "voti": [18, 16, 19]},
    {"nome": "Elena", "voti": [24, 26]},
]
soglia = 20

print(studenti_media_se_hanno_voto_alto(studenti, 18))



