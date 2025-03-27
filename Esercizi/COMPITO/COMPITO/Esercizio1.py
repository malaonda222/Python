# Esercizio 1
'''Scrivere un programma che permetta all'utente di inserire una serie di parole in input, terminando 
l'inserimento quando viene digitata la parola "fine" (che non deve essere considerata nell'elaborazione). 
Per ogni parola inserita, il programma deve verificare se il primo e l'ultimo carattere sono uguali e 
visualizzare un messaggio corrispondente.'''

# impostare il ciclo while
while True:
    parola:str = input("Inserisci una parola: ") # chiedere all'utente di inserire una parola
    if parola == "fine": # condizione per cui il programma termina
        break
    else:
        if parola[0] == parola[-1]: # condizione per verificare che il primo carattere e l'ultimo siano uguali
            print(f"Il primo e l'ultimo carattere della parola {parola} sono uguali") # output


# '''Esercizio corretto'''
while True:
    # Chiedo all'utente di inserire una parola da verificare
    parola:str = input("Inserire una parola per verificare se è palindroma: ").lower()

    # Controllo se l'utente ha inserito "fine" per terminare il programma
    if parola == "fine":
        break

    # Controllo se la parola è palindroma
    if parola == parola[::-1]:
        print("La parola è palindroma")
    # Se la parola non è palindroma
    else:
        print("La parola non è palindroma")
    