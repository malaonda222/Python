'''
Statistiche
 
Scrivi una funzione con il seguente header:
 
* calculate_stats(nums: list[float]) -> dict[str, float]:
 
che, data una lista di numeri, ritorni un dizionario con tre chiavi:
 
* "min" -> il valore minimo della lista
* "max" -> il valore massimo della lista
* "avg" -> la media aritmetica (somma diviso numero di elementi)
 
Se la lista è vuota, solleva un'eccezione ValueError con messaggio "lista vuota"
 
Attenzione, i valori min. max e avg non possono essere calcolati usando funzioni built-in di python o altre librerie.
'''

def calculate_stats(nums: list[float]) -> dict[str, float]:
    if not nums:
        raise ValueError("Lista vuota")
    
    minimo: float = nums[0]
    massimo: float = nums[0]
    somma: float = 0.0
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
        "avg": float(media)
        }

print(calculate_stats([3.4, 6.7, 9.0]))