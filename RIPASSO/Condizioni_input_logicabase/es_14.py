'''
Traccia:
Crea una funzione conta_lettere() -> None che:
* Chiede all’utente una frase tramite input().
* Analizza solo i caratteri alfabetici (isalpha()).
* Conta quante vocali (a, e, i, o, u) ci sono.
* Conta quante consonanti ci sono.
* Ignora spazi, numeri, simboli e punteggiatura.
Alla fine stampa:
* Numero totale di vocali
* Numero totale di consonanti
'''


def conta_lettere() -> None:
    numero_vocali = 0
    numero_consonanti = 0 
    vocali = ["a", "e", "i", "o", "u"]

    frase: str = input("Inserisci una frase: ")

    for element in frase:
        if element.isalpha():
            if element.lower() in vocali:
                numero_vocali += 1 
            else:
                numero_consonanti += 1 

    return f"Numero vocali: {numero_vocali}\nNumero consonanti: {numero_consonanti}"

print(conta_lettere())