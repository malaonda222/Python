'''Scrivere un programma che permetta all'utente di inserire una serie di parole in input, terminando 
l'inserimento quando viene digitata la parola "fine" (che non deve essere considerata nell'elaborazione). 
Per ogni parola inserita, il programma deve verificare se il primo e l'ultimo carattere sono uguali e 
visualizzare un messaggio corrispondente.'''

while True:
    parola:str = input("Inserire una parola per verificare se è palindroma: ")
    if parola == "fine":
        break

    if parola == parola[::-1]:
        print("La parola è palindroma.")
    else:
        print("La parola non è palindroma.")