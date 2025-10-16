'''
Data in input una lista di numeri interi o float, la funzione deve restituire un 
dizionario con informazioni sui valori: minimo, massimo e somma.
 
Nome dell’esercizio: analyze_numbers
Traccia:
Scrivi una funzione con il seguente header:
* def analyze_numbers(nums: list[float]) -> dict[str, float]:
 
La funzione deve restituire un dizionario con quattro chiavi:
* "min" → il numero più piccolo della lista
* "max" → il numero più grande della lista
* "sum" → la somma di tutti i numeri
* "average" → la media dei numeri
 
Vincoli:
Non usare funzioni built-in come min(), max(), sum() o simili.
Non usare librerie esterne.
 
Se la lista è vuota, solleva un’eccezione ValueError con messaggio "lista vuota".
'''

def analyze_numbers(nums: list[float]) -> dict[str, float]:
    if len(nums) == 0:
        raise ValueError("Lista vuota")

    minimo = nums[0]
    massimo = nums[0]
    somma = 0.0
    for num in nums:
        if num < minimo:
            minimo = num 
        if num > massimo:
            massimo = num 
        somma += num 
    media = somma / len(nums)
    return {
        "min": float(minimo),
        "max": float(massimo),
        "sum": float(somma),
        "average": float(media)
    }