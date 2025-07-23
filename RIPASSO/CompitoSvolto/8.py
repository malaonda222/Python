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
lista_numeri = []
while i <= 5:
    valore = input(f"Inserisci il {i}° numero: ")
    if valore.lstrip('-').isdigit():
        valore = int(valore)
        if 1 <= valore <= 30:
            lista_numeri.append(valore)
            i += 1
        else:
            print("Inserire un numero compreso tra 1 e 30")
print(lista_numeri)


# versione con try/except
i = 1 
lista_numeri = []
while i <= 5:
    valore = input(f"Inserisci il {i}° numero: ")
    try:
        valore = int(valore)
        if 1 <= valore <= 30:
            lista_numeri.append(valore)
            i += 1
        else:
            print("Inserire un numero intero compreso tra 1 e 30")
    except ValueError:
        print("Inserire un numero intero valido")
print(lista_numeri)



asterischi = 0 
for numero in lista_numeri:
    asterischi = numero * "*"
    print(asterischi)