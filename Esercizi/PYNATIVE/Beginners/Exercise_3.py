# Print characters present at an even index number

# chiedi all'utente di inserire una parola
stringa = input("Inserisci una parola: ")

# definisci la variabile lunghezza per indicare la lunghezza della stringa
lunghezza = len(stringa)

# imposta ciclo for con range per stampare solo le lettere pari
for item in range(0, lunghezza-1, 2):
    print(stringa[item])