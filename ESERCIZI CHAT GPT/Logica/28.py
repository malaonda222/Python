from string import ascii_uppercase, ascii_lowercase 

'''Scrivi una funzione verifica_password(password) che:
    Restituisce True se la password soddisfa i seguenti requisiti:
        Almeno 8 caratteri
        Contiene almeno una lettera maiuscola
        Contiene almeno una lettera minuscola
        Contiene almeno un numero
        Contiene almeno un carattere speciale (es. !@#$%^&*)

    Altrimenti restituisce False'''

def verifica_password(password: str) -> bool:
    occorrenze_minuscole = 0
    occorrenze_maiuscole = 0
    occorrenze_numero = 0
    occorrenze_speciale = 0

    if len(password) < 8:
        return False
    for element in password:
        if element in ascii_lowercase:
            occorrenze_minuscole += 1
        if element in ascii_uppercase:
            occorrenze_maiuscole += 1
        if element.isdigit():
            occorrenze_numero += 1
        if element in "!@#$%^&*":
            occorrenze_speciale += 1
    
    if occorrenze_minuscole < 1 or occorrenze_maiuscole < 1 or occorrenze_numero < 1 or occorrenze_speciale < 1:
        return False 
    else:
        return True 
    
print(verifica_password("Lon98$pl"))
    