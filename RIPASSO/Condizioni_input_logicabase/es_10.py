'''
Scrivi una funzione media_numeri_positivi() che:
* Chiede numeri interi all’utente in un ciclo infinito.
* Termina quando l’utente scrive "stop".
* Tiene conto solo dei numeri maggiori di zero.
Alla fine stampa:
* Il numero di valori positivi inseriti
* La media aritmetica dei numeri positivi
* Se non è stato inserito nessun numero positivo, stampa un messaggio specifico.
'''

def media_numeri_positivi():
    numeri_positivi = []
    
    while True:
        numero = input("Inserisci un numero: ")
        if numero.lower() == "stop":
            break 
        numero = int(numero)
        if numero < 0:
            raise ValueError("Il numero deve essere maggiore di 0")
        else: 
            contatore_positivi += 1
            numeri_positivi.append(numero)
    
    if not numeri_positivi:
        return "Nessun numero positivo inserito"
    
    media = sum(numeri_positivi) / len(numeri_positivi)

    return len(numeri_positivi), media

media_numeri_positivi()
