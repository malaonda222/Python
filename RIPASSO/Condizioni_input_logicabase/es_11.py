'''Scrivi una funzione chiamata conta_pari_dispari() che:
* Chiede all’utente di inserire numeri interi, uno alla volta.
* Termina quando l’utente digita "stop" (insensibile a maiuscole/minuscole).
* Conta quanti numeri pari e quanti dispari sono stati inseriti.
* Ignora i numeri non validi (es. "ciao"), mostrando un messaggio d’errore.
Alla fine stampa:
* Il numero totale di valori validi
* Quanti erano pari
* Quanti erano dispari
'''
 
def conta_pari_dispari():
    cont_pari = 0
    cont_dispari = 0
    cont_totale = 0
    while True:
        valore = input("Inserisci un numero intero oppure 'stop' per interrompere: ")
        if valore.lower() == 'stop':
            break 

        try: 
            valore = int(valore)
        except ValueError:
            return "valore non valido. Inserisci solo numeri interi o 'stop' per interrompere!"

        if valore % 2 == 0:
            cont_pari += 1
            cont_totale += 1
        else:
            cont_dispari += 1
            cont_totale += 1
    return f"Conteggio totale: {cont_totale}\nConteggio pari: {cont_pari}\nConteggio dispari: {cont_dispari}"

print(conta_pari_dispari())