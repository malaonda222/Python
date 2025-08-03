'''Mini-progetto: Simula un gestionale di contatti con dizionario {nome: numero}:
    Aggiungi contatto
    Cancella contatto
    Cerca contatto
    Mostra tutti'''

contatti: dict = {"Mario": "365236596", "Lina": "3336985421"}
while True:
    print("\n---MENU---")
    print("1. Aggiungi contatto")
    print("2. Cancella contatto")
    print("3. Cerca contatto")
    print("4. Mostra tutti")
    print("5. Esci dal programma")

    scelta: str = input("Scegli un'opzione: ")

    if scelta == "1":
        nome: str = input("Inserisci il nome da aggiungere: ")
        telefono: str = input("Inserisci il numero di telefono da aggiungere: ")
        contatti[nome] = telefono 
        print("Contatto aggiunto")
    
    elif scelta == "2":
        nome_da_eliminare: str = input("Inserisci il nome del contatto da eliminare: ")
        if nome_da_eliminare in contatti:
            del contatti[nome_da_eliminare]
            print("Contatto eliminato con successo")
        else:
            print("Il contatto non è presente nella lista dei contatti")
    
    elif scelta == "3":
        nome_da_cercare: str = input("Inserisci il nome da cercare: ")
        if nome_da_cercare in contatti:
            print("Contatto trovato")
        else:
            print("Contatto non presente nella lista dei contatti")
    
    elif scelta == "4":
        if not contatti:
            print("Lista dei contatti vuota")
        else:
            for key, value in contatti.items():
                print(f"{key}: {value}")
        
    elif scelta == "5":
        print("uscita dal programma")
        break 

    else:
        print("Scelta non valida. Inserisci un'opzione tra 1 e 5")

