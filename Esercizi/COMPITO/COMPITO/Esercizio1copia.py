'''Scrivere un programma che permetta all'utente di inserire una serie di parole in input, terminando 
l'inserimento quando viene digitata la parola "fine" (che non deve essere considerata nell'elaborazione). 
Per ogni parola inserita, il programma deve verificare se il primo e l'ultimo carattere sono uguali e 
visualizzare un messaggio corrispondente.'''

while True:
    parola = input("Inserire una parola: ")
    if parola == "fine":
        print("Fine del programma.")
        break 
    else:
        if parola[0] == parola[-1]:
            print("Il primo e l'ultimo carattere sono uguali.")
        