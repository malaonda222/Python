'''Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali non negativi 
(sia interi che decimali). 
L'inserimento termina quando viene fornito un numero negativo, che funge da sentinella e non deve essere 
considerato nei calcoli.
Il programma deve:
1. Calcolare la media dei soli numeri interi inseriti. Utilizzate la funzione is_integer() per verificare 
se il numero inserito è un intero.
2. Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli inseriti 
(sia interi che decimali).'''

lista_interi = []
lista_decimali = []
lista_generale = []
somma_interi = 0
cont_interi = 0
numero_max = 0
numero_min = 0



while True:
    numero = float(input("Inserisci un valore alla lista del numeri: "))
    if numero < 0: 
        print("Errore. Inserire un numero reale non negativo.")
        continue
    else:
        if numero.is_integer():
            lista_generale.append(numero)
            lista_interi.append(numero)
            cont_interi += 1
            somma_interi += numero
            media = somma_interi/cont_interi

        else:
            lista_generale.append(numero)
            lista_decimali.append(numero)
   
    print(f"La media dei numeri è {media}.")

    lista_generale = lista_interi + lista_decimali
    numero_min = min(lista_generale)
    numero_max = max(lista_generale)
    
    print(f"Il numero più piccolo è: {numero_min}.")
    print(f"Il numero più grande è: {numero_max}")



        

