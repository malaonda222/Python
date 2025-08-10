'''Logica: Scrivi una funzione che richiede input finché l’utente non inserisce un intero.'''

def numero_intero():
    while True:
        valore = input("Inserisci un valore intero: ")
        try:
            valore = int(valore)
            break
        except ValueError:
            print("Per favore inserire un valore valido (numero intero)")
        
    return f"Il numero inserito è: {valore}"

print(numero_intero())