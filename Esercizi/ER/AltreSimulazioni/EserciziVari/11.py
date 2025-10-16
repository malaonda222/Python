'''Scrivi una funzione chiamata calculate_root_mean_square_deviation(nums: list[float]) -> float che calcola la deviazione quadratica media 
(RMSD - Root Mean Square Deviation) di una lista di numeri.

La deviazione quadratica media si calcola così:
Calcola la media dei numeri.
Per ogni numero nella lista, calcola la differenza tra il numero e la media.
Eleva al quadrato ciascuna differenza.
Calcola la media dei quadrati delle differenze.
Calcola la radice quadrata del risultato.
'''

def calculate_root_mean_square_deviation(nums: list[float]) -> float:
    somma = 0.0
    for num in nums: 
        somma += num 
    media = somma / len(nums)

    somma_quadrati = 0.0
    conteggio = 0
    for num in nums:
        somma_quadrati += (num - media)**2 
        conteggio += 1 
    media_quadrati = somma_quadrati / conteggio 
    return media_quadrati**0.5





