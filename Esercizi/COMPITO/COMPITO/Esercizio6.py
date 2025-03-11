# Esercizio 6
'''Scrivere un programma che acquisisca in input due numeri interi, n1 e n2, e calcoli il prodotto di tutti 
i numeri compresi tra n1 e n2, inclusi gli estremi.
Il programma deve gestire anche il caso in cui n1 > n2, calcolando comunque il prodotto correttamente.'''

# chiedere all'utente di inserire due numeri interi
n1 = int(input("Inserisci il primo numero intero: "))
n2 = int(input("Inserisci il secondo numero intero: "))

if n1 % 1 != 0 and n2 % 1 != 0: # condizione che stabilisce se entrambi i numeri sono interi
    print("Errore. Inserisci due numeri interi.")
else: 
    prodotto = 1
    if n1 < n2: # condizione per il caso in cui n1 < n2
        i = n1
        for i in range (n1, n2 + 1):
            prodotto *= i
        print(f"Il prodotto è: {prodotto}") # stampa del risultato

    elif n1 > n2: # condizione per il caso in cui n1 > n2
        i = n1
        for i in range (n2, n1 + 1):
            prodotto *= i
        print(f"Il prodotto è: {prodotto}") # stampa del risultato