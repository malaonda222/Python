# Esercizio 1
'''Scrivere un programma che permetta all'utente di inserire una serie di parole in input, terminando 
l'inserimento quando viene digitata la parola "fine" (che non deve essere considerata nell'elaborazione). 
Per ogni parola inserita, il programma deve verificare se il primo e l'ultimo carattere sono uguali e 
visualizzare un messaggio corrispondente.'''

# impostare il ciclo while
while True:
    parola = input("Inserisci una parola: ") # chiedere all'utente di inserire una parola
    if parola == "fine": # condizione per cui il programma termina
        break
    else:
        if parola[0] == parola[-1]: # condizione per verificare che il primo carattere e l'ultimo siano uguali
            print(f"Il primo e l'ultimo carattere della parola {parola} sono uguali") # output