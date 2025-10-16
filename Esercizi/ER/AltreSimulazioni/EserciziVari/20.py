'''
Traccia esercizio: scale_to_range
Tema: Normalizzazione e trasformazioni di liste di numeri
 
Obiettivo:
Scrivi una funzione che prende in input una lista di numeri e un intervallo [new_min, new_max] 
e restituisce una nuova lista in cui tutti i valori sono scalati nel nuovo intervallo, secondo la formula:
 
valore_scalato = new_min + (x - min) / (max - min) * (new_max - new_min)
 
Nome dell’esercizio: scale_to_range
Header della funzione:
def scale_to_range(values: list[float], new_min: float, new_max: float) -> list[float]:

Regole: 
* Non usare funzioni built-in come min(), max(), map() o simili.
* Se la lista è vuota, solleva ValueError("lista vuota").
* Se tutti i valori della lista sono uguali (quindi max == min), 
solleva ZeroDivisionError("impossibile scalare: valori uguali").
 
Esempio:
scale_to_range([10, 20, 30], 0, 100)  # ➜ [0.0, 50.0, 100.0]
scale_to_range([5, 5, 5], 0, 10)      # ➜ solleva ZeroDivisionError
'''

def scale_to_range(values: list[float], new_min: float, new_max: float) -> list[float]:
    if not values:
        raise ValueError("Lista vuota.")
    
    minimo = values[0]
    massimo = values[0]
    nuova_lista = []

    for num in values:
        if num < minimo:
            minimo = num 
        if num > massimo:
            massimo = num 
    
    for num in values:
        valore_scalato = new_min + (num - minimo) / (massimo - minimo) * (new_max - new_min)
        nuova_lista.append(valore_scalato)

    if massimo == minimo:
        raise ZeroDivisionError("Impossibile scalare: valori uguali")

    return nuova_lista

print(scale_to_range([10, 20, 30], 0, 100)) 