'''
Tema: Analisi di una lista di dizionari
Obiettivo:
Data in input una lista di dizionari contenenti informazioni su persone ({"nome": str, "età": int}), 
la funzione deve restituire un dizionario con i dati di età più giovane, più vecchia e media.
 
Nome dell’esercizio: analyze_people
Traccia:
Scrivi una funzione con il seguente header: 
* def analyze_people(people: list[dict[str, int]]) -> dict[str, any]:
 
La funzione deve restituire un dizionario con queste chiavi:
* "youngest" → il nome della persona più giovane
* "oldest" → il nome della persona più vecchia
* "average_age" → l’età media delle persone

Vincoli:
Non usare funzioni built-in come min(), max(), sorted() o simili.
Non usare librerie esterne.
 
Se la lista è vuota, solleva un’eccezione ValueError con messaggio "lista vuota".
'''

def analyze_people(people: list[dict[str, int]]) -> dict[str, any]:
    if not people:
        raise ValueError("Lista vuota.")
    
    
    eta_minima = persona[0]["eta"]
    eta_massima = persona[0]["eta"]
    piu_giovane = persona[0]["nome"] 
    piu_vecchia = persona[0]["nome"]
    somma_eta = 0.0
    conteggio = 0

    for persona in people:
        nome = persona["nome"]
        eta = persona["eta"]
        if eta < eta_minima:
            eta_minima = eta 
            piu_giovane = nome
        if eta > eta_massima:
            eta_massima = eta 
            piu_vecchia = nome 
        somma_eta += eta 
        conteggio += 1
    eta_media = somma_eta / conteggio
    return {
        "youngest": piu_giovane,
        "oldest": piu_vecchia,
        "average_age": eta_media
    }
