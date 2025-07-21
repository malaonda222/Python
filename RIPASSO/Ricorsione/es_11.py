'''Scrivi una funzione ricorsiva che stampa i numeri da n a 1.'''

def stampa_decrescente(n: int):
    if n == 0:
        return 0
    else:
        print(n)
        stampa_decrescente(n - 1)
    
stampa_decrescente(5)