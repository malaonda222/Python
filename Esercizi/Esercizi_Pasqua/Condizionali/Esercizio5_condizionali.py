def integerPower(base:int, esponente:int)  -> int:
    if esponente <= 0 or esponente % 1 != 0:
        return ("Errore. Inserire un numero intero positivo diverso da zero.")
    else:
        return base ** esponente 
    
def integerPower(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return result