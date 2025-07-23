'''Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali non negativi 
(sia interi che decimali). 
L'inserimento termina quando viene fornito un numero negativo, che funge da sentinella e non deve essere 
considerato nei calcoli.
Il programma deve:
1. Calcolare la media dei soli numeri interi inseriti. Utilizzate la funzione is_integer() per verificare 
se il numero inserito è un intero.
2. Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli inseriti 
(sia interi che decimali).'''

numeri_interi = []
numeri_totali = []

while True:
    input_utente: float = float(input("Inserisci un numero non negativo: "))
    if input_utente < 0:
        break 
    else:
        if not input_utente.is_integer():
            print("Il numero inserito non è intero")
            numeri_totali.append(input_utente)
        else:
            input_utente = int(input_utente)
            numeri_interi.append(input_utente)
            numeri_totali.append(input_utente)

numero_max = max(numeri_totali)
numero_min = min(numeri_totali)
media = sum(numeri_interi) / len(numeri_interi)

print(f"Numero massimo: {numero_max}")
print(f"Numero minimo: {numero_min}")
print(f"Media: {media:.2f}")
