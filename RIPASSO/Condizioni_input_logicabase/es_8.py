'''
Scrivi una funzione chiamata somma_dispari() che: 
* Chiede all’utente un numero intero positivo maggiore di 0.
* Calcola la somma di tutti i numeri dispari compresi tra 1 e quel numero (incluso).
* Stampa il risultato finale.
'''

def somma_dispari() -> None:
    numero: int = int(input("Inserisci un numero intero positivo: "))
    if numero <= 0:
        raise ValueError("Errore. Il numero deve essere maggiore di 0")
    somma_dispari = 0
    for i in range(1, numero+1):
        if i % 2 != 0:
            somma_dispari += i 
    return f"La somma dei numeri dispari compresi tra 1 e {numero} è: {somma_dispari}"

print(somma_dispari())
