''' 
Scrivi una funzione somma_primi_n(n: int) -> int che: 
Prende un numero intero n come argomento.
Calcola la somma dei primi n numeri interi positivi, cioè da 1 a n inclusi. 
Restituisce il risultato.
(Se vuoi puoi fare anche una versione con input() ma ti consiglio 
di farla prima con parametro, per abituarti alla scrittura di 
funzioni riutilizzabili)
'''

def somma_primi_n(n: int) -> int:
    somma_numeri = 0
    for i in range(1, n+1):
        somma_numeri += i 
    print(somma_numeri)

somma_primi_n(5)
somma_primi_n(10)