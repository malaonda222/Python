'''
Traccia:
Scrivi una funzione che chiede all’utente una serie di numeri interi (termina con "fine").
Alla fine stampa la media dei numeri dispari inseriti. 
Se non è stato inserito alcun numero dispari, stampa "Nessun numero dispari inserito".
'''

def media_dispari() -> int:
    somma_dispari = 0
    contatore_dispari = 0
    while True:
        input_utente = input("Inserisci un numero: ")
        if input_utente.lower() == 'fine':
            break
        if input_utente.lstrip("-").isdigit():
            input_utente = int(input_utente)
            if input_utente % 2 != 0:
                somma_dispari += input_utente
                contatore_dispari += 1
        else:
            print("Inserisci un numero intero!")
        
    if contatore_dispari < 0:
        print("Nessun numero dispari inserito")
    else:
        print(f"Media dei numeri dispari inseriti:{somma_dispari/contatore_dispari}")

media_dispari()