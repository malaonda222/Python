'''Titolo dell’esercizio
Analisi delle altezze delle persone

Obiettivo
Data in input una lista di dizionari contenenti informazioni su persone, ognuna con nome e altezza in centimetri (espressa come float), la funzione deve restituire un dizionario
con le seguenti informazioni:
- Il nome della persona più alta
- Il nome della persona più bassa
- L’altezza media

Header della funzione: def analyze_heights(people: list[dict[str, float]]) -> dict[str, any]:

Struttura della lista in input
Ogni dizionario della lista avrà questa struttura:
{"nome": str, "altezza": float}

Requisiti
Non usare funzioni già pronte come min(), max(), sorted(), sum(), statistics o simili
Non usare librerie esterne
Se la lista è vuota, solleva ValueError("lista vuota")'''


def analyze_heights(people: list[dict[str, float]]) -> dict[str, any]:
    if not people:
        raise ValueError("Lista vuota.")
    
    new_dict = {}
    altezza_max = people[0]["altezza"]
    altezza_min = people[0]["altezza"]

    piu_alta = people[0]["nome"]
    piu_bassa = people[0]["nome"]
    somma_eta = 0.0 

    for persona in people:
        if persona["altezza"] > altezza_max:
            altezza_max = persona["altezza"]
            piu_alta = persona["nome"]
        if persona["altezza"] < altezza_min:
            altezza_min = persona["altezza"]
            piu_bassa = persona["nome"]
        somma_eta += persona["altezza"]

    media = somma_eta / len(people)
    new_dict["Tallest"] = piu_alta
    new_dict["Shortest"] = piu_bassa
    new_dict["Average"] = media 

    return new_dict

lista_persone = [
    {"nome": "Roberta", "altezza": 175.8}, 
    {"nome": "Luigi", "altezza": 180.6},
    {"nome": "Lisa", "altezza": 150.0}
]
print(analyze_heights(lista_persone))