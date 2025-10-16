'''
Nome dell’esercizio: filter_and_upper
Traccia:
Scrivi una funzione chiamata filter_and_upper che prende in input:
* words: lista di stringhe
* min_len: intero che rappresenta la lunghezza minima
 
La funzione deve:
* Filtrare tutte le stringhe nella lista la cui lunghezza è maggiore o uguale a min_len.
* Convertire tutte le stringhe filtrate in maiuscolo.
* Restituire una stringa unica con le parole filtrate concatenate, separate da uno spazio " "
'''

def filter_and_upper(words: list[str], min_len: int) -> str:
    nuova_lista = []
    for word in words:
        if len(word) >= min_len:
            word_upper = word.upper() 
            nuova_lista.append(word_upper)
    return " ".join(nuova_lista)

words = ["come", "ti", "chiami"]
print(filter_and_upper(words, 3))

