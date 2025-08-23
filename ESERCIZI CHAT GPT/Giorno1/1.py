'''Esercizio 1 - Somma delle cifre
Scrivi una funzione somma_cifre(n) che prende un numero intero positivo e restituisce la somma delle sue cifre.
Esempio: somma_cifre(1234) → 10'''

def somma_cifre() -> int:
    input_utente = input("Inserisci un numero: ")
    try: 
        input_utente = int(input_utente)
        if input_utente <= 0: 
            print("Il numero deve essere maggiore di zero")
            return 
    except ValueError:
        print("Il numero deve essere intero!")
        return 
    
    somma = 0
    for element in str(input_utente):
        somma += int(element) 
    print(somma) 

somma_cifre()