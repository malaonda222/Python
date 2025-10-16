'''Scrivi una funzione chiamata
calculate_weighted_average(values: list[float], weights: list[float]) -> float
che calcoli la media ponderata dei valori nella lista values, usando i pesi corrispondenti nella lista weights.

Le due liste devono avere la stessa lunghezza.
Se una delle liste è vuota, solleva un ValueError.
Se la somma dei pesi è 0, solleva un ZeroDivisionError.'''

def calculate_weighted_average(values: list[float], weights: list[float]) -> float:
    if len(values) != len(weights):
        raise ValueError("Errore. Le due liste devono avere la stessa lunghezza.")
    if not values or not weights:
        raise ValueError("Errore. Entrambe le liste devono essere valorizzate.")
    if sum(weights) == 0:
        raise ZeroDivisionError("La lista dei pesi non può essere 0")
    else:
        somma = 0.0
        for i in range(len(values)):
            somma += values[i] * weights[i]
        return somma

        # oppure 
        # for i in range(len(values)):
        #     moltiplicazione = values[i] * weights[i]
        #     somma += moltiplicazione
        #     return somma


values = [70, 80, 90]        
weights = [0.2, 0.3, 0.5]  
print(calculate_weighted_average(values, weights))