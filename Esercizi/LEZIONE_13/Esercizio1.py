'''Scrivere in Python una funzione recursivePower che calcola la potenza di un numero utilizzando la ricorsione. La funzione deve ricevere due parametri in input:

base: il numero da elevare a potenza.
exponent: l’esponente a cui elevare la base.'''

def recursivePower(base:int, exponent:int) -> None:
    
    # if base == 0: non è necessrio
    #     return 0
    if exponent == 0:
        return 1
    elif base == 0 and exponent == 0:
        return 0
    else:
        return int(base * recursivePower(base, exponent-1))

print(recursivePower(3, 4))
print(recursivePower(4, 3))
print(recursivePower(2, 5))
print(recursivePower(5, 2))


def recursivePower(base:int, esponente:int) -> int:
    if base == 0:
        return 0
    if esponente == 0:
        return 1
    else:
        return int(base * recursivePower(base, esponente-1 ))
    
print(recursivePower(5, 2))