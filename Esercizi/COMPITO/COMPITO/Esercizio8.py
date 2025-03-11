# Esercizio 8
'''Un'applicazione interessante dei computer è la rappresentazione grafica di dati.
Scrivere un programma che acquisisca cinque numeri interi (ognuno compreso tra 1 e 30) e visualizzi in output un grafico a barre testuale 
con asterischi *.
Per ogni numero letto, il programma deve stampare una riga contenente tanti asterischi quanti il valore del numero stesso.

Esempio di output:
Se l'utente inserisce i numeri 5, 8, 3, 12, 7, il programma deve stampare:

*****
********
***
************
*******'''

# costruzione del ciclo che permetta di inserire 5 numeri interi
for i in range (5):
    n = float(input("Inserisci un numero intero compreso tra 1 e 30: "))
    if n % 1 == 0 and 1 <= n <= 30: # condizione per verificare se il numero è intero e compreso tra 1 e 30
        n_int = int(n) 
        print("*" * n_int) # stampa degli asterischi relativi al numero inserito dall'utente

    else: # condizione che verifica tutti gli altri casi
        print("Errore! Inserisci un numero intero compreso tra 1 e 30.")
