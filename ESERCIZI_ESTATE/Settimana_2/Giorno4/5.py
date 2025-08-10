'''Crea una lambda che calcola il quadrato di un numero.'''

def quadrato(n: int) -> int:
    risultato = lambda n: n**2
    return risultato(n)

print(quadrato(8))

def cubo(n: int) -> int:
    result = lambda n: n**3 
    return result(n)

print(cubo(10))


