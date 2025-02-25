# nome = input("Inserisci il nome: ")
# ruolo = input("Inserisci il ruolo: ")
# età = input("Inserisci l'età: ")

# chiedere all'utente nome, ruolo ed età
user:dict = {"nome": input("Inserisci il nome: "), "ruolo": input("Inserisci il ruolo: "), "età": int(input("Inserisci l'età: "))}

# match statement
match user:
    case {"nome": name, "ruolo": "admin", "età": age}:
        print("Accesso completo a tutte le funzionalità.")
    case {"nome": name, "ruolo": "moderatore", "età": age}:
        print(f"Salve {user['nome']}. Può gestire i contenuti ma non modificare le impostazioni.")
    case {"nome": name, "ruolo": "utente adulto", "età": age} if age >= 18:
        print("Accesso standard a tutti i servizi.")
    case {"nome": name, "ruolo": "utente minorenne", "età": age} if age < 18:
        print("Accesso limitato! Alcune funzionalità sono bloccate.")
    case {"nome": name, "ruolo": "ospite", "età": age}:
        print(f"Ciao {name}, il tuo accesso è ristretto! Solo visualizzazione dei contenuti.")
    case _:
        print("Attenzione! Il ruolo non riconosciuto! Accesso Negato!")
