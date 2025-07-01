'''Scrivi una funzione che calcoli la potenza di un numero base
elevato a un esponente.'''

def potenza(base:int, esponente:int) -> int:
    if base == 0:
        return 0
    if esponente == 0:
        return 1
    else: 
        return int(base * potenza(base, esponente - 1))
    
print(potenza(3, 4))