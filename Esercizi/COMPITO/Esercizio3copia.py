'''Scrivere un programma che acquisisca una stringa inserita dall'utente e generi una nuova stringa che 
corrisponda alla versione invertita della stringa originale. Il programma deve poi visualizzare la stringa 
ottenuta in output. Per risolvere il problema non si deve utilizzare alcun tipo di funzione, ma esclusivamente
 i cicli.'''

frase = input("Inserisci una stringa a piacere: ")
frase_invertita = " "

for x in range(len(frase) -1, -1, -1):
    frase_invertita += frase[x]

print(frase_invertita)

