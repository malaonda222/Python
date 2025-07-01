# esercizio con opzione repeat until

#legge il primo valore
sum = 0
i = 0

#ciclo per 5 iterazioni
while True:
    n:int = int(input("Inserisci un numero: ")) #legge il numero
    if n>0: #controlla se è maggiore
        sum+=n
    i+=1 #incrementa contatore
    if i==5: #condizione di uscita
        break 

#stampa del risultato
print(f"La somma dei cinque valori è: {sum}")