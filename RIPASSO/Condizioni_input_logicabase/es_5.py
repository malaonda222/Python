'''Scrivi una funzione richiedi_password() che:
Chiede all’utente di inserire una password.
Continua a chiedere finché non rispetta tutte le condizioni: 
* Deve contenere almeno 8 caratteri
* Deve contenere almeno una lettera
* Deve contenere almeno un numero
Quando la password è valida:
* Stampa "Password accettata"
* Ritorna la password
'''

def richiedi_password() -> None:
    password: str = input("Inserisci una password: ")
    if len(password) >= 8 and any(i.isalpha() for i in password) and any(i.isdigit() for i in password):
        print("Password accettata")
        print(f"La password è: {password}")
    else:
        return False
    
richiedi_password()