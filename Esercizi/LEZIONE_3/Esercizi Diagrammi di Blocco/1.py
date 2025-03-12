# Sistema di gestione per un parcheggio 

max_posti = int(input("Inserisci il numero massimo di posti: "))
liberi = max_posti

while True:
    opzione = input(f"Inserisci un'opzione tra \"ingresso\", \"uscita\", \"stato\", \"esci\": ").lower()
    match opzione:
        case "ingresso":
            if liberi > 0:
                liberi = liberi - 1
                print("Prego, entrare nel parcheggio.")
            else:
                print("Sfortunatamente non ci sono posti disponibili.")
        case "uscita":
            if liberi < max_posti:
                liberi = liberi + 1
                print("Si è liberato un posto.")
            else:
                print("Tutti i posti sono già disponibili.")
        case "stato":
            print(f"I posti liberi sono: {liberi}")
            print(f"I posti occupati sono: {max_posti - liberi}")
        case "esci":
            print("Il programma termina.")
            break 
        case _: 
            print(f"Input non corretto. Prego riprovare.")
    
