'''
Scrivi una funzione analizza_numero() che:
Chieda all’utente un numero (anche negativo).
Restituisca:
"Positivo" se il numero è maggiore di zero.
"Negativo" se è minore di zero.
"Zero" se è uguale a zero.
'''
 
def analizza_numero() -> None:
    n: float = float(input("Inserisci un numero (anche negativo): "))
    if n > 0:
        print("Positivo")
    elif n < 0:
        print("Negativo")
    else:
        print("Zero")

analizza_numero()