'''Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali non negativi 
(sia interi che decimali). 
L'inserimento termina quando viene fornito un numero negativo, che funge da sentinella e non deve essere 
considerato nei calcoli.
Il programma deve:
1. Calcolare la media dei soli numeri interi inseriti. Utilizzate la funzione is_integer() per verificare 
se il numero inserito è un intero.
2. Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli inseriti 
(sia interi che decimali).'''

somma_interi:int = 0
cont_interi:int = 0
numero_max:int = 0
numero_min:int = 0
lista_interi = []
lista_decimali = []
lista_generale = []

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

# opzione due
somma:int = 0 # Somma dei numeri interi
counter_interi:int = 0  # Contatore dei numeri interi inseriti
massimo:float = float('-inf') # Inizializzo il massimo a -infinito
minimo:float = float('inf') # Inizializzo il minimo a +infinito

while True:
    # Chiedo all'utente di inserire un numero
    n:float = float(input("Inserire un numero: "))

    # Controllo se l'utente ha inserito un numero negativo per terminare il programma
    if n < 0:
        print("Programma terminato.")
        break
    # Se il numero è positivo
    else:
        # Controllo se il numero è intero
        if n.is_integer():
            counter_interi += 1
            somma += int(n)

        # Controllo se il numero è maggiore o minore del massimo e del minimo
        if n > massimo:
            massimo = n # Aggiorno il massimo
        if n < minimo: 
            minimo = n # Aggiorno il minimo

# Calcolo e stampo la media dei soli numeri interi, solo se sono stati inseriti numeri interi
if counter_interi > 0:
    media:float = somma / counter_interi
    print(f"La media dei soli numeri interi vale: {media}")

# Controllo se il massimo e il minimo sono stati aggiornati rispetto ai valori iniziali
if massimo != float('-inf') and minimo != float('inf'):
    # Stampo il massimo e il minimo
    print(f"Valore massimo inserito: {massimo}")
    print(f"Valore minimo inserito: {minimo}")

        
