# Esercizio 10
'''Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall'utente.

Il programma deve:

1. acquisire una sequenza di numeri interi, terminando l'inserimento quando l'utente digita 0 (che non deve essere considerato nei calcoli);
2. calcolare e visualizzare la somma di tutti i numeri pari inseriti;
3. calcolare e visualizzare la media di tutti i numeri dispari inseriti;
4. determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista); 
5. se più numeri hanno la stessa frequenza massima, visualizzarli tutti.

Output:
Somma dei numeri pari: 10
Media dei numeri dispari: 5.67
Numero più frequente: 7 (2 volte)'''

somma_pari = 0
somma_dispari = 0
media_dispari = 0
i = 0
lista_numeri = []

# ciclo while che permetta di inserire tanti numeri quanti ne desidera l'utente
while True:
    numero = float(input("Inserisci un numero (0 per terminare): "))
    if numero == 0: # condizione che permette all'utente di uscire dal ciclo
        print("Il programma termina!")
        break 
    elif numero % 1 != 0: # condizione per verificare se il numero inserito non sia intero
        print("Errore. Inserire un numero intero.")
    else: # condizione che permette di raccogliere i numeri interi che verranno inseriti nella lista dei numeri interi
        numero_int = int(numero)
        lista_numeri.append(numero_int)
        print(lista_numeri)

        if numero_int % 2 == 0: # condizione per stabilire se il numero intero è pari
            somma_pari += numero_int 
        else: # condizione per il caso in cui il numero intero sia dispari
            somma_dispari += numero_int
            i = i + 1
            media_dispari = somma_dispari/i 

# stabilire il numero più frequente nella lista e la sua frequenza nella lista
num_frequenti = []
max_frequenze = 0
for x in lista_numeri:
    frequenza_x = lista_numeri.count(x)
    if max_frequenze < frequenza_x:
        num_frequenti = []
        max_frequenze = frequenza_x
        num_frequenti.append(x)
    elif max_frequenze == frequenza_x:
        if x not in num_frequenti:
            num_frequenti.append(x)

# stampare i risultati ottenuti
print(f"La somma dei numeri pari è: {somma_pari}")
print(f"La media dei numeri dispari è: {media_dispari}")
print(f"Numero/i più frequente/i: {num_frequenti} ({max_frequenze} volta/e)")

dizionario_frequenze = {}
while True:
    numero_inserito = int(input("Inserisci il numero: "))
    if numero_inserito in dizionario_frequenze:
        dizionario_frequenze[numero_inserito] += 1 #il numero si trova all'interno del dizionario
    else:
        dizionario_frequenze[numero_inserito] = 1 #il numero non si trova all'interno del dizionario

        
