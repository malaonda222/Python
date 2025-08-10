'''Logica: Simula un calcolatore che accetta operazioni via lambda (+, -, *, /)'''

def addizione(a: int, b: int) -> int:
    risultato = lambda a, b: a + b 
    return risultato(a, b)

def sottrazione(c: int, d: int) -> int:
    result = lambda a, b: a - b 
    return result(c, d)

def moltiplicazione(e: int, f: int) -> int:
    risultato2 = lambda e, f: e * f
    return risultato2(e, f)

def divisione(g: int, h: int) -> int:
    result2 = lambda g, h: g / h
    return result2(g, h)

print(addizione(3, 4))
print(sottrazione(9, 10))
print(moltiplicazione(9, 3))
print(divisione(4, 2))