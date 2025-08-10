'''Gestisci la divisione per zero con try/except.'''

def divisione(a: int, b: int) -> float:
    try: 
        risultato = a / b 
    except ZeroDivisionError:
        print("Errore. Entrambi i numeri devono essere diversi da zero")
        return None
    return risultato 

print(divisione(10, 5))
print(divisione(0, 3))