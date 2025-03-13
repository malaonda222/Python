'''Sistema di registrazione degli studenti ai corsi'''
nome_corso = input("Inserisci il nome del corso: ")
max_posti = 100

while True: 
    opzione = input("Inserisci un'opzione a scelta tra \"iscrivi\", \"annulla\", \"visualizza\", \"elimina\", \"esci\": ")
    match opzione:
        case "iscrivi":
            if max_posti > 0:
                max_posti = max_posti - 1
                print(f"Iscrizione avvenuta con successo al corso di {nome_corso}.")
            else:
                print(f"Non ci sono posti disponibili per il corso di {nome_corso}.")
        case "annulla":
            if max_posti < 100:
                max_posti = max_posti + 1
                print("Annullamento avvenuto con successo.")
            else:
                print(f"Tutti i posti sono già disponibili per il corso di {nome_corso}.")
        case "visualizza":
            print(f"I posti liberi rimasti per il corso di {nome_corso} sono: {max_posti}.")
            print(f"I posti occupati per il corso di {nome_corso} sono: {100-max_posti}.")
        case "elimina":
            max_posti = 100
            nome_corso = input("Inserisci il nome del corso: ")
            break
        case "esci":
            print("Il programma termina.")
            break
        case _:
            print("Input non riconosciuto. Inserire un valore valido.")