'''Richiedi un input numerico e gestisci errori di conversione.'''

def input_numerico():
    input_utente = input("Inserisci un numero: ")
    try: 
        input_utente = int(input_utente)
    except ValueError:
        print("Inserisci un valore numerico!")
        return None
    return input_utente

print(input_numerico())