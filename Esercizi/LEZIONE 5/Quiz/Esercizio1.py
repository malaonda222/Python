def prime_factors(n: int) -> list[int]:

    lista_fattori = []
 
    while n % 2 == 0:
        lista_fattori.append(2)
        n = n // 2
    
    i = 3
    while i * i <= n:
        while n % i == 0:
            lista_fattori.append(i)
            n = n // i
        i += 2 
    
    if n > 2:
        lista_fattori.append(n)
    return lista_fattori
 
print(prime_factors(4))
print(prime_factors(60))

#  soluzione Profe
def prime_factors(n:int) -> list[int]:    
    """Restituisce una lista dei fattori primi del numero intero positivo n."""
    fattori = []
    divisore = 2
    while n > 1:
        while n % divisore == 0:
            fattori.append(divisore)
            n = n // divisore
        divisore += 1
    return fattori

print(prime_factors(60))