'''Lancia un ValueError se un input non è valido.'''

def input_non_valido():
    while True: 
        input_utente = input("Inserisci un valore: ")
        try: 
            input_utente = float(input_utente)
            break
        except ValueError:
            raise ValueError("Input non valido. Prego riprovare")
    return input_utente

print(input_non_valido())