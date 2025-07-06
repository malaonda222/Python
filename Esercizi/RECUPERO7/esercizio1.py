def baricentro(v: list[int]) -> int | None:
    somma_totale = sum(v)
    somma_sinistra = 0
    for i in range(len(v)):
        somma_sinistra += v[i]
        somma_destra = somma_totale - somma_sinistra
        if somma_sinistra == somma_destra:
            return i 
    return None 

def printResult(v: list[int]) -> bool:
    i = baricentro()
    if i is None:
        print(f"Il baricentro del vettore = {v} non esiste!")
    else:
        print(f"Esiste il baricentro del vettore v = {v} ed è dato dall'indice {i}.")