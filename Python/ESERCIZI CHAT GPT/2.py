# Classificare un mese
mese:str = input("Inserisci il mese dell'anno: ").lower()

# match statement
match mese:
    case "dicembre"|"gennaio"|"febbraio":
        print("Inverno")
    case "marzo"|"aprile"|"maggio":
        print("Primavera")
    case "giugno"|"luglio"|"agosto":
        print("Estate")
    case "settembre"|"ottobre"|"novembre":
        print("Autunno")
    case _:
        print("Mese non riconosciuto.")

