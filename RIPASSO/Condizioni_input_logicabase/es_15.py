'''
Traccia:
Crea una funzione conta_fuori_intervallo() -> None che:
* Chiede all’utente di inserire numeri interi uno alla volta.
* L’inserimento termina quando l’utente digita "stop".
* Per ogni numero inserito, controlla se non è compreso tra 10 e 100 (inclusi).
Alla fine, stampa:
* Il numero totale di valori inseriti.
* Quanti di questi sono fuori intervallo.
* Quanti sono dentro l’intervallo.
'''

def conta_fuori_intervallo() -> None:
    lista_numeri = []
    fuori_intervallo = 0
    dentro_intervallo = 0

    while True:
        input_utente = input("Inserisci numero: ")
        if input_utente == "stop":
            break 
        try:
            input_utente = int(input_utente)
            lista_numeri.append(input_utente)
            if 10 <= input_utente <= 100:
                dentro_intervallo += 1
            else:
                fuori_intervallo += 1
        except ValueError:
            return "Errore. Il numero deve essere intero" 
        
    return f"Il numero totale di valori inseriti è: {len(lista_numeri)}\nFuori intervallo: {fuori_intervallo}\nDentro intervallo: {dentro_intervallo}"


print(conta_fuori_intervallo())