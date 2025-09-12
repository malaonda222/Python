def leggi_o_crea_file():
    nome_file = input("Inserisci il nome del file: ")
    try:
        with open(nome_file, 'r') as file:
            contenuto = file.read()
            print("Contenuto del nuovo file: ")
            print(contenuto)
            
    except FileNotFoundError:
        print("File non trovato. Crea automaticamente: ")
        with open(nome_file, 'w') as file:
            file.write("File creato automaticamente")
        print("File creato con successo.")

        with open(nome_file, 'r') as file:
            contenuto = file.read()
            print("Contenuto del nuovo file:")
            print(contenuto)



        