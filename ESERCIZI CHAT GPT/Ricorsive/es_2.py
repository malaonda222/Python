'''Scrivi una funzione che verifichi se un numero n è un numero primo.
Un numero primo è un numero maggiore di 1 che è divisibile per 1 e se stesso. '''

def primo(numero:int, divisore=None) -> None:
    if numero <= 1:
        return False
    if divisore is None:
        divisore = 2
    if divisore * divisore > numero:
        return True
    if numero % divisore == 0:
        return False 
    return primo(numero, divisore + 1)
