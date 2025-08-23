# Messaggi
testo = input("Inserisci il tipo di messaggio: ")
contenuto = input("Inserisci il contenuto del messaggio: ")

messaggio = {"tipo": testo, "sentence": contenuto}

match messaggio: 
    case {"tipo": "testo", "sentence": contenuto}:
        print(f"Messaggio di testo ricevuto: {contenuto}")
    case {"tipo": "immagine", "sentence": contenuto}:
        print(f"Immagine ricevuta: {contenuto}")
    case {"tipo": "video", "sentence": contenuto}:
        print(f"Video ricevuto: {contenuto}")
    case _:
        print("tipo di messaggio non riconosciuto.")