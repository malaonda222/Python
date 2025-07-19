'''
Traccia:
Scrivi una funzione che continua a chiedere all’utente dei numeri interi 
finché non digita "stop".
A quel punto stampa la somma solo dei numeri positivi inseriti.
'''

def positivi_inseriti() -> int:
    somma_pos = 0
    while True:
        valore = input("Inserisci un numero: ")
        if valore.lower() == "stop":
            return somma_pos
        try:
            valore = int(valore)
            if valore > 0:
                somma_pos += valore 
        except:
            print("Inserisci un numero valido oppure 'stop' per uscire")

print(positivi_inseriti())
