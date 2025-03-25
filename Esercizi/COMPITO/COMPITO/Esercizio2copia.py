'''Scrivere un programma che acquisisca una stringa inserita dall'utente e calcoli il numero totale 
di spazi presenti nella stringa. Il risultato deve essere visualizzato in output.'''

stringa = input("Inserisci una frase: ")
count_spazi = 0
for item in stringa:
    if item == " ":
        count_spazi += 1
print(f"Il numero totali di spazi nella stringa è: {count_spazi}.")

string = input("Inserisci una stringa: ")
spazi = string.count(" ")
print(spazi)
