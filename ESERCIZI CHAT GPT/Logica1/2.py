'''Anni bisestili
Chiedi un anno e stampa se è bisestile (regole: divisibile per 4, ma non per 100 a meno che non sia anche divisibile per 400)'''

def is_bisestile() -> bool:
    input_utente: str = input("Inserisci l'anno: ")
    try: 
        input_utente = int(input_utente)
        if input_utente <= 0:
            return False
        else:
            if (input_utente % 4 == 0 and not input_utente % 100 == 0) or (input_utente % 400 == 0):
                return True
            else:
                return False
    except ValueError:
        print("Inserisci un anno valido!")
        return False 
    
if is_bisestile():
    print("L'anno è bisestile")
else:
    print("L'anno non è bisestile")