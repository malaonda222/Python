'''Titolo dell’esercizio: Analisi dei numeri pari e dispari
Obiettivo
Scrivi una funzione che prende in input una lista di numeri interi e restituisce un dizionario con le seguenti informazioni:

Il numero pari più piccolo
Il numero dispari più grande
Il conteggio totale dei numeri pari
Il conteggio totale dei numeri dispari

Header della funzione
def analyze_even_odd(nums: list[int]) -> dict[str, int | None]:

Requisiti
Non puoi usare funzioni già pronte come min, max, filter, sorted o simili
Se la lista è vuota, devi sollevare un ValueError con il messaggio "lista vuota"
Se non ci sono numeri pari o dispari, per quei valori nel dizionario puoi restituire None'''


def analyze_even_odd(nums: list[int]) -> dict[str, int | None]:
    if not nums:
        raise ValueError("Lista vuota.")
    
    even_min = None 
    odd_max = None 
    conteggio_even = 0
    conteggio_odd = 0
    for num in nums:
        if num % 2 == 0:
            if even_min == None or num < even_min:
                even_min = num 
            conteggio_even += 1
        elif num % 2 != 0:
            if odd_max == None or num > odd_max:
                odd_max = num 
            conteggio_odd += 1 

    return {
        "Numero pari più piccolo": even_min,
        "Numero dispari più grande": odd_max,
        "Conteggio totale numeri pari": conteggio_even,
        "Conteggio totale numeri dispari": conteggio_odd
    }

