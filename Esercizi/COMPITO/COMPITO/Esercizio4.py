# Esercizio 4
'''Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali non negativi 
(sia interi che decimali). 
L'inserimento termina quando viene fornito un numero negativo, che funge da sentinella e non deve essere 
considerato nei calcoli.
Il programma deve:
1. Calcolare la media dei soli numeri interi inseriti. Utilizzate la funzione is_integer() per verificare 
se il numero inserito è un intero.
2. Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli inseriti 
(sia interi che decimali).'''

media = 0
somma_interi = 0
numero = 0
numeri_interi = []
numeri_decimali = []
conta_interi = 0

# impostare ciclo while
while numero >= 0:
    numero = float(input("Inserire una sequenza di numeri reali non negativi: ")) # chiedere all'utente di inserire un numero
    
    if numero < 0: # condizione per numero negativo che non considera i numeri negativi
        print("Esci dal programma.")

    else: # condizione per tutti gli altri casi
        if numero.is_integer(): # verificare che il numero inserito sia intero
            somma_interi += numero
            conta_interi += 1
            media = somma_interi/conta_interi
            numeri_interi.append(numero)
            
        else: # condizione per i numeri decimali
            numeri_decimali.append(numero)

# determinare numero massimo e numero minimo
numero_max = 0
numero_min = 0

numeri = numeri_interi + numeri_decimali
numero_max = max(numeri)
numero_min = min(numeri)

# stampa dei risultati
print("\nRisultati: ")               
print(f"La media dei numeri interi inseriti è {media}")
print(f"Il numero più grande è: {numero_max}")
print(f"Il numero minimo è: {numero_min}")




        

    
