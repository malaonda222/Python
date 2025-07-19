'''
Traccia:
Crea una funzione somma_positivi() -> None che:
* Chiede all’utente di inserire numeri interi (uno alla volta).
* Termina l’inserimento se l’utente scrive 'stop'.
Se il numero è:
* positivo → lo somma
* negativo → lo ignora
* zero → stampa 'Hai inserito zero, non viene contato.' e lo ignora
* Alla fine stampa la somma totale dei numeri positivi inseriti.
'''

def somma_positivi() -> None:
    somma_totale = 0
    while True:
        valore = input("Inserisci un numero intero: ")
        if valore == 'stop':
            break 
        try: 
            valore = int(valore)
        except ValueError:
            print(f"Input non valido. Inserisci un numero intero o stop")
            continue 

        if valore > 0:
            somma_totale += valore 
        if valore == 0:
            print("Hai inserito zero, non viene contato")
         
    print(f"La somma dei numeri positivi è: {somma_totale}")

somma_positivi()