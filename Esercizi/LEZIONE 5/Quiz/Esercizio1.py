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