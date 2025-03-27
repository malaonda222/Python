# Esercizio 2
'''Scrivere un programma che acquisisca una stringa inserita dall'utente e calcoli il numero totale 
di spazi presenti nella stringa. Il risultato deve essere visualizzato in output.'''

# # chiedere all'utente di inserire una stringa
# stringa = input("Inserisci una stringa: ")

# # calcolo del numero totale di spazi presenti nella stringa
# spazi = stringa.count(" ")

# # stampa il numero totale di spazi nella stringa
# print(f"Il numero totale di spazi presenti nella stringa sono: {spazi}")


# Chiede all'utente di inserire una stringa
stringa:str = input("Digitare una stringa: ")
# Inizializza un contatore di caratteri spazio
counter_spazi:int = 0

# Iterazione su ogni carattere della stringa
for i in range(len(stringa)):
    # Controlla se un carattere della stringa sia uguale al carattere di spazio " "
    if stringa[i] == " ":
        # Incrementa di uno il contatore di caratteri spazio
        counter_spazi += 1

print(f"Nella stringa: \"{stringa}\" ci sono {counter_spazi} spazi")