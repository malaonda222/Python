# Esercizio 2
'''Scrivere un programma che acquisisca una stringa inserita dall'utente e calcoli il numero totale 
di spazi presenti nella stringa. Il risultato deve essere visualizzato in output.'''

# chiedere all'utente di inserire una stringa
stringa = input("Inserisci una stringa: ")

# calcolo del numero totale di spazi presenti nella stringa
spazi = stringa.count(" ")

# stampa il numero totale di spazi nella stringa
print(f"Il numero totale di spazi presenti nella stringa sono: {spazi}")