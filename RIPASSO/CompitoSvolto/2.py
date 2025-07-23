'''Scrivere un programma che acquisisca una stringa inserita dall'utente e calcoli il numero totale 
di spazi presenti nella stringa. Il risultato deve essere visualizzato in output.'''

input_utente: str = input("Inserire una stringa: ")
conta_spazi:int = 0
for element in input_utente:
    if element == " ":
        conta_spazi += 1
    else:
        continue 
print(f"Il numero di spazi nella stringa sono: {conta_spazi}")


stringa: str = input("Inserire una stringa: ")
conta_spazi: int = 0
for i in range(len(stringa)):
    if stringa[i] == " ":
        conta_spazi += 1 
print(f"Nella stringa '{stringa}' ci sono {conta_spazi} spazi")