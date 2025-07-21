'''Scrivi una funzione ricorsiva potenza(base, esponente) che calcoli base
elevato a esponente'''

def recursive_potenza(base: int, esponente: int) -> int:
    if esponente == 0 and base == 0:
        raise ValueError("Indefinita")
    if esponente == 0:
        return 1
    if base == 0:
        return 0
    else:
        return base * recursive_potenza(base, esponente - 1)
    
print(recursive_potenza(2, 3)) 