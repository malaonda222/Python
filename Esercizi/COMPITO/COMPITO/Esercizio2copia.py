'''Scrivere un programma che acquisisca una stringa inserita dall'utente e calcoli il numero totale 
di spazi presenti nella stringa. Il risultato deve essere visualizzato in output.'''

stringa:str = input("Inserisci una frase: ")
count_spazi:int = 0
for item in range(len(stringa)):
    if stringa[item] == " ":
        count_spazi += 1
print(f"Il numero totali di spazi nella stringa \"{stringa}\" è: {count_spazi}.")
