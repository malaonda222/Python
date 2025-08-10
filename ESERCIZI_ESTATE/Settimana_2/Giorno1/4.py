'''Restituisci True se un numero è perfetto.'''

def numero_perfetto(n: int) -> bool:
    divisori_senza_resto = []
    for i in range(1, n):
        if n % i == 0:
            divisori_senza_resto.append(i)
    if n == sum(divisori_senza_resto):
        return True
    else:
        return False 
    
print(numero_perfetto(28))
print(numero_perfetto(30))


def numero_perfetto2(n: int) -> bool:
    return n == sum(i for i in range(1, n) if n % i == 0)

print(numero_perfetto2(28))
print(numero_perfetto2(80))