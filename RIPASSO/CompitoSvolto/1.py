'''Scrivere un programma che permetta all'utente di inserire una serie di parole in input, terminando 
l'inserimento quando viene digitata la parola "fine" (che non deve essere considerata nell'elaborazione). 
Per ogni parola inserita, il programma deve verificare se il primo e l'ultimo carattere sono uguali e 
visualizzare un messaggio corrispondente.'''

while True:
    valore: str = input("Inserisci ua parola: ")
    if valore.lower() == 'fine':
        break
    else:
        if valore[0] == valore[-1]:
            print("La prima e l'ultima lettera della parola sono uguali!")
        else:
            print("La prima e l'ultima lettera della parola non sono uguali!")

