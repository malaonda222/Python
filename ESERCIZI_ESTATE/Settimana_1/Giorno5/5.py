'''Conta le vocali in una stringa usando un ciclo for.'''

contatore = 0
input_utente: str = input("Inserisci una parola: ")
for i in range(len(input_utente)):
    if input_utente[i] in "aeiou":
        contatore += 1 
print(contatore)


contatore = 0
input_ut: str = input("Inserisci una stringa: ")
for i in input_ut:
    if i in "aeiou":
        contatore += 1
print(contatore)