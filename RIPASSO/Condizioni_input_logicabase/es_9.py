'''
Traccia:
Scrivi una funzione chiamata conta_fino_a_stop() che:
* Chiede all’utente di inserire numeri uno alla volta.
* Continua a chiedere numeri finché l’utente non scrive "stop" 
(maiuscole/minuscole non contano).
* Ignora eventuali valori non numerici (es: "ciao"), mostrando un messaggio d’errore.
* Alla fine, stampa quanti numeri validi sono stati inseriti.
'''
 
def conta_fino_a_stop() -> int:
    contatore_numeri = 0
    while True:
        valore = input("Inserisci un numero: ")
        if valore.lower() == "stop":
            break 
        try:
            valore = float(valore)
            contatore_numeri += 1
        except ValueError:
            print("Errore. Input non valido. Inserisci un numero o 'stop'")
            continue
    return contatore_numeri

print(conta_fino_a_stop())
        
