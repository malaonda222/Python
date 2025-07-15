'''
Titolo: "Controllo età per l'accesso a un evento"
Scrivi una funzione chiamata controlla_eta che:
Chieda all'utente la sua età (usando input()).
Stabilisca:
* Se l'età è minore di 14, stampa: "Accesso vietato."
* Se è tra 14 e 17, stampa: "Accesso con accompagnatore."
* Se è 18 o più, stampa: "Accesso consentito."
'''

def controllo_eta() -> None:
    eta: int = int(input("Inserisci la tua età: "))
    if eta < 0:
        raise ValueError("Numero non riconosciuto")
    if eta < 14:
        print("Accesso vietato")
    elif 14 <= eta <= 17:
        print("Accesso con accompagnatore")
    elif eta >= 18:
        print("Accesso consentito")

controllo_eta()
    