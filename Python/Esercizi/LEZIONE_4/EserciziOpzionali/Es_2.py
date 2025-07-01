'''Indovina il gioco dei numeri:
Creare una funzione che genera un numero casuale all'interno di un intervallo specificato dall'utente.
Consentire all'utente di indovinare il numero entro un numero massimo specificato di tentativi.
Fornire feedback all'utente dopo ogni ipotesi, indicando se la loro ipotesi è troppo alta, troppo bassa o corretta.
Terminare il ciclo quando l'utente indovina correttamente il numero o raggiunge il numero massimo di tentativi.
'''
import random

def numero_casuale(numero_min: int, numero_max: int, tentativi: int) -> None:
    if numero_min >= numero_max:
        print("Errore: il numero minimo deve essere inferiore al numero massimo.")
        return
    else:
        numero_da_indovinare: int = random.randint(numero_min, numero_max)
        print(f"Il numero da indovinare è compreso tra {numero_min} e {numero_max}. Hai {tentativi} tentativi.")
    
        i = 0
        while i < tentativi: 
            try: 
                numero_prova = int(input("Indovina il numero: "))
            except ValueError:
                print("Inserisci un numero intero valido.")
                continue
            
            if numero_prova == numero_da_indovinare:
                print("Hai indovinato il numero!")
                break
            elif numero_prova < numero_da_indovinare:
                print("Ipotesi troppo bassa. Riprovare.")
                i = i + 1
            else:
                print("Ipotesi troppo alta. Riprovare.")
                i = i + 1
                    
        else:
            print(f"Tentativi terminati, il numero da indovinare era: {numero_da_indovinare}. Hai perso.")

prova1 = numero_casuale(-3, 27, 5)


