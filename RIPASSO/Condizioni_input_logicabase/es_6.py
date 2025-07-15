'''
Scrivi una funzione conta_fino_a() che:
- Chiede all’utente di inserire un numero intero positivo N
- Stampa tutti i numeri da 1 fino a N inclusi, uno per riga
- Se il numero non è positivo o non è un intero, stampa un messaggio d’errore
Suggerimenti:
* Usa range(1, N + 1) per generare i numeri da 1 a N
* Ricorda che range(1, 6) produce: 1, 2, 3, 4, 5
* Controlla che N > 0 prima di iniziare a stampare
'''

def conta_fino() -> None:
    numero: int = int(input("Inserisci un numero intero positivo: "))
    if numero < 0:
        raise ValueError("Il numero deve essere intero positivo")
    
    for i in range(1, numero+1):
        print(f"{i}") 
        

conta_fino()

