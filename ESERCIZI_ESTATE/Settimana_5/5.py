'''Scrivere un programma che:
Chieda all’utente il nome di un file esistente.
Legga tutte le righe del file.
Rimuova tutte le righe vuote o contenenti solo spazi.
Sovrascriva il file originale con il contenuto pulito.
Stampi un messaggio di conferma e mostri il nuovo contenuto.'''


def rimuovi_righe_vuote():
    nome_file = input("Inserisci il nome del file: ")

    try:
        with open(nome_file, 'r') as file:
            righe = file.readlines()
            print(f"Righe del file: {''.join(righe)}")
        
        righe_pulite = [riga for riga in righe if riga.stip() != ""]
        
        with open(nome_file, 'w') as file:
             file.writelines(righe_pulite)
        
        print("Righe vuote rimosse. Nuovo contenuto: ")
        for riga in righe_pulite:
            print(riga.strip())
            
    except FileNotFoundError:
        print("Il file specificato non è stato trovato")


rimuovi_righe_vuote()