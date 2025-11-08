'''Scrivi una funzione che riceve una lista di parole (words) e un intero (n).
La funzione deve contare e restituire quante parole nella lista hanno una lunghezza maggiore o uguale a n. def count_long_words(words: list[str], n: int) -> int: if not words: return 0 else: conteggio = 0 for word in words: if len(word) >= n: conteggio += 1 return conteggio'''

def count_long_words(words: list[str], n: int) -> int: 
    if not words: 
        return 0 
    else: 
        conteggio = 0 
        for word in words: 
            if len(word) >= n: 
                conteggio += 1 
        return conteggio