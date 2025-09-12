'''Scrivere un programma che:
Chieda all’utente il nome di un file di testo.
Apre il file.
Conta e stampa:
Il numero di righe.
Il numero di parole.
Il numero di caratteri totali (spazi inclusi).'''

def conta_statistiche_file():
    nome_file = input("Inserisci il nome di un file: ")

    try: 
        with open(nome_file, 'r') as file:
            righe = file.readlines()
            
            num_righe = len(righe)
            parole = 0
            caratteri_totali = 0
            
            for riga in righe: 
                parole += len(riga.split())
                caratteri_totali += len(riga)
                
            print("Statistiche del file:")
            print(f"- Righe: {num_righe}")
            print(f"- Parole: {parole}")
            print(f"- Caratteri: {caratteri_totali}")
    
    except FileNotFoundError:
        print("Errore: file specificato non esistente")
    
conta_statistiche_file()