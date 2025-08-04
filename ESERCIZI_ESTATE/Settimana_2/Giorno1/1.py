'''Scrivi una funzione che calcola il fattoriale.'''

def fattoriale() -> int:
    while True:
        n = input("Inserisci il numero: ")
        try: 
            n = int(n)
            if n < 0:
                print("Errore, il numero deve essere positivo")
            else:
                print(f"Numero scelto: {n}")
                break
        except ValueError:
            print("Inserisci un valore valido")
    