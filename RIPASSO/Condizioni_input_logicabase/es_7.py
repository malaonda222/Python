'''Crea una funzione chiamata stampa_numeri_primi() che:
* Chiede all’utente un numero intero positivo.
* Controlla che l'input sia valido (deve essere un intero > 1).
* Stampa tutti i numeri primi da 2 fino a quel numero, uno per riga.'''

def stampa_numeri_primi() -> None:
    numero: int = int(input("Inserisci un numero intero positivo: "))
    if numero < 1:
        raise ValueError("Il numero deve essere positivo")
    for i in range(2, numero+1):
        primo = True 
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                primo = False 
                break 
        if primo: 
            print(i)

stampa_numeri_primi()