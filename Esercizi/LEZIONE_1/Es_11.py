# Sistema di prenotazione posti
liberi = 20
while True:
    opzione = input(f"Inserisci un'opzione valida a scelta tra \"prenota\", \"libera\", \"visualizza\", \"esci\": ").lower()

    if opzione == "prenota":
        if liberi > 0:
            liberi = liberi - 1
            print("Prenotazione avvenuta con successo.")
        else:
            print("Non ci sono posti disponibili.")

    elif opzione == "libera":
        if liberi < 20:
            liberi = liberi + 1
            print("Posto liberato con successo.")
        else:
            print("Tutti i posti sono già disponibili.")

    elif opzione == "visualizza":
        print(f"I posti liberi sono {liberi}")
        print(f"I posti occupati sono: {20 - liberi}")

    elif opzione == "esci":
        print("Il programma termina.")
        break    
    else:
        print(f"Input non riconosciuto. Prego riprovare.")