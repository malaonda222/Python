'''
Esercizio: Funzione calculate_mean_absolute_deviation
 
Scrivi una funzione con il seguente header:
* calculate_mean_absolute_deviation(nums: list[float]) -> float
 
Descrizione:
La funzione prende una lista di numeri nums e calcola la deviazione assoluta media (MAD), 
ossia la media delle differenze assolute di ciascun numero rispetto alla media della lista.
Passaggi:
    * Calcola la media dei valori nella lista.
    * Per ogni valore nella lista, calcola la differenza assoluta tra il valore e la media.
    * Calcola la media di tutte queste differenze assolute.
    * Restituisci questo valore.
 
Vincoli:
    * Se la lista è vuota, solleva un’eccezione ValueError con messaggio "lista vuota".
    * Non usare funzioni built-in come sum(), abs(), min(), max() o librerie esterne; 
    devi implementare tutto manualmente.
 
Esempio:
nums = [1.0, 2.0, 3.0, 4.0, 5.0]

# Media:
(1+2+3+4+5)/5 = 3.0
 
# Differenze assolute rispetto alla media:
|1-3|=2, |2-3|=1, |3-3|=0, |4-3|=1, |5-3|=2
 
# Media delle differenze assolute:
(2+1+0+1+2)/5 = 1.2
 
# Risultato:
1.2
'''

def calculate_mean_absolute_deviation(nums: list[float]) -> float:
    if not nums:
        raise ValueError("Lista vuota")
    
    somma = 0
    for num in nums:
        somma += num 
    media = somma/len(nums)

    somma_diff_assoluta = 0
    conteggio = 0
    for num in nums:
        differenza = num - media 
        if differenza < 0:
            differenza = -differenza
        somma_diff_assoluta += differenza
        # oppure 
        # somma_diff_assoluta += differenza if differenza >= 0 else -differenza
        conteggio += 1
    mad = somma_diff_assoluta / conteggio 

    return float(mad)



