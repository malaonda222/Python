'''
Traccia:
Scrivi una funzione conta_pari_dispari_zero() -> None che:
* Chieda all’utente di inserire numeri interi uno alla volta.
* Il ciclo continua fino a che l’utente scrive "fine".
Per ogni numero:
* Se è zero, conta quanti zero sono stati inseriti.
* Se è pari diverso da zero, incrementa un contatore dei pari.
* Se è dispari, incrementa un contatore dei dispari.
* Alla fine, stampa i tre totali.
'''

def conta_pari_dispari_zero() -> None:
    cont_zero = 0
    cont_pari = 0
    cont_dispari = 0
    while True:
        valore = input("Inserisci un numero intero: ")
        if valore.lower() == 'fine':
            break 
        try:
            valore = int(valore)
            if valore == 0:
                cont_zero += 1
            elif valore % 2 == 0:
                cont_pari += 1
            else:
                cont_dispari += 1
        except ValueError:
            print("Inserisci un numero intero!")
        
    print(f"Contatore zero: {cont_zero}\nContatore pari: {cont_pari}\nContatore dispari: {cont_dispari}")

conta_pari_dispari_zero()