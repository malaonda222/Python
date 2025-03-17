# Ruoli
name = input("Inserisci il tuo nome: ")
funzione = input("Inserisci il tuo ruolo: ")

utente = {"nome": name, "ruolo": funzione}

match utente:
    case {"nome": name, "ruolo": "amministratore"}:
        print(f"{name}, hai accesso completo al sistema.")
    case {"nome": "Luca", "ruolo": "moderatore"}:
        print("Luca puoi gestire i contenuti.")
    case {"nome": name, "ruolo": "utente"}:
        print(f"{name}, hai accesso limitato alle funzionalità.")
    case _:
        print("Ruolo non riconosciuto. Contatta l'amministratore.")