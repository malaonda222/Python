'''
Scrivi una funzione chiamata
* calculate_normalized_scores(scores: list[float]) -> list[float]
 
che restituisca una nuova lista con tutti i punteggi normalizzati tra 0 e 1, secondo la formula:
valore normalizzato = x - min / max - min

Regole:
 
Se la lista è vuota, solleva ValueError("lista vuota").
 
Se tutti i valori nella lista sono uguali (quindi max == min), solleva un 
ZeroDivisionError("impossibile normalizzare: valori uguali")

Esempio:
 
calculate_normalized_scores([10, 20, 30])  # ➜ [0.0, 0.5, 1.0]
'''

def calculate_normalized_scores(scores: list[float]) -> list[float]:
    if not scores:
        raise ValueError("Lista vuota.")
    
    massimo = scores[0]
    minimo = scores[0]

    for score in scores:
        if score > massimo:
            massimo = score 
        if score < minimo:
            minimo = score 
    
    if massimo == minimo:
        raise ZeroDivisionError("Impossibile normalizzare: valori uguali.")
    
    nuova_lista = []
    for score in scores:
        punteggio_normalizzato = (score - minimo) / (massimo - minimo) 
        nuova_lista.append(punteggio_normalizzato)

    return nuova_lista