def baricentro(v: list[int]) -> int | None:
    for i in range(len(v)):
       if sum(v[:i]) == sum(v[i+1:]):
           return i 
       else:
           return None

def printResult(v: list[int]) -> bool:
    i = baricentro(v)
    if i is None:
        print(f"Il baricentro del vettore = {v} non esiste!")
    else:
        print(f"Esiste il baricentro del vettore v = {v} ed è dato dall'indice {i}!")

def baricentroOttimizzato(v: list[int]):
    totale = 0
    for i in range(len(v)):
        totale += i 
    somma_sinistra = 0
    for i in range(len(v)):
        somma_sinistra += v[i]
        somma_destra = totale - somma_sinistra
        if somma_sinistra == somma_destra:
            return f"Esiste il baricentro del vettore v = {v} ed è dato dall'indice {i}"
        else:
            return f"Il baricentro del vettore = {v} non esiste!" 
    
    return totale



vettore1 = [1, 2, 3, 2, 5, 2, 1]
printResult(vettore1)

vettore2 = [2, 0, -1, 4, 6, 3, -1]
printResult(vettore2)

print(baricentroOttimizzato(vettore1))
print(baricentroOttimizzato(vettore2))