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

i = 1
count_n = 1
lista_numeri = []

for i in range(5):
        numero = input(f"Inserisci il {count_n}° numero: ")
        if numero.lstrip('-').isdigit():
            numero = int(numero)
            if 1 <= numero <= 30:
                lista_numeri.append(numero)
                count_n += 1
       
        else:
            print("Errore. Inserisci un numero compreso tra 1 e 30.")

        


