# Esercizio 3
'''Scrivere un programma che acquisisca una stringa inserita dall'utente e generi una nuova stringa che 
corrisponda alla versione invertita della stringa originale. Il programma deve poi visualizzare la stringa 
ottenuta in output. Per risolvere il problema non si deve utilizzare alcun tipo di funzione, ma esclusivamente
 i cicli.'''

# chiedere all'utente di inserire una stringa
stringa = input("Inserire una stringa: ")
stringa_invertita = ""

# ciclo for per invertire l'ordine dei caratteri della stringa
for x in range(len(stringa) -1, -1, -1):
    stringa_invertita += stringa[x]

# stampa la stringa invertita
print(stringa_invertita)



