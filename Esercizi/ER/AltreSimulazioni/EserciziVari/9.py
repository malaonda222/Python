'''
Esercizio: Funzione analyze_numbers

Obiettivo:
Data una lista di numeri interi o float, la funzione deve restituire un 
dizionario con informazioni sui valori: minimo, massimo, primo e ultimo numericamente.

Nome dell’esercizio: analyze_numbers
Traccia:
Scrivi una funzione con il seguente header:
* def analyze_numbers(nums: list[float]) -> dict[str, float]:

La funzione deve restituire un dizionario con quattro chiavi:
    * "min_value" → il numero più piccolo della lista
    * "max_value" → il numero più grande della lista
    * "first_positive" → il primo numero positivo che appare nella lista
    * "last_negative" → l’ultimo numero negativo che appare nella lista
 
Vincoli:
* Non usare funzioni built-in come min(), max(), sorted() o simili.
* Non usare librerie esterne.

* Se la lista è vuota, solleva un’eccezione ValueError con messaggio "lista vuota".
* Se non ci sono numeri positivi o negativi, puoi restituire None per quelle chiavi.'''


def analyze_numbers(nums:list[float]) -> dict[str, float]:
    if len(nums) == 0:
        raise ValueError("Lista vuota")
    else:
        min_value = nums[0]
        max_value = nums[0]
        first_positive = None 
        last_negative = None 

        for num in nums: 
            if num < min_value:
                min_value = num 
            if num > max_value:
                max_value = num 
            if num > 0 and first_positive == None:
                first_positive = num 
            if num < 0:
                last_negative = num 
        return {
            "min value": float(min_value),
            "max value": float(max_value),
            "first positive": float(first_positive),
            "last negative": float(last_negative)
        }
    

nums = [1.4, 6.7, 8.3, -1.2, -3.2]
print(analyze_numbers(nums))