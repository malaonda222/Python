'''
Crea una funzione verifica_coppie() -> None che:
* Chieda all’utente di inserire numeri interi, uno alla volta.
* Termini l’inserimento quando l’utente digita "stop".
* Analizzi le coppie di numeri consecutivi inseriti (es. il primo e il secondo, il 
secondo e il terzo, ecc.).
* Conti quante coppie hanno almeno un numero pari.
* Stampi il numero totale di coppie trovate e quante tra queste soddisfano la condizione.
Se l’utente inserisce meno di due numeri, stampare: "Non ci sono abbastanza numeri 
per formare coppie."
'''

def verifica_coppie() -> None:
    lista_numeri = []
    while True: 
        input_utente = input("Inserisci un numero intero: ")
        if input_utente.lower() == 'stop':
            break 
        try:
            input_utente = int(input_utente)
            lista_numeri.append(input_utente)
        except ValueError:
            return "Il numero deve essere un intero"
        
    if len(lista_numeri) < 2:
        return "Non ci sono abbastanza anumeri per formare coppie"
    
    totale_coppie = len(lista_numeri) - 1
    conta_coppie = 0
    for i in range(len(lista_numeri) -1):
        if lista_numeri[i] % 2 == 0 or lista_numeri[i-1] % 2 == 0:
            conta_coppie += 1 

    return f"Numero totale delle coppie: {totale_coppie}\nCoppie con almeno un numero pari: {conta_coppie}"


print(verifica_coppie())