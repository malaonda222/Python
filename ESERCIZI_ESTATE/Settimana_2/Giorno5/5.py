'''Scrivi una funzione robusta che gestisce tutti gli errori.'''

def funzione_robusta():
    try: 
        nome_file = input("Inserisci il nome del file da leggere: ")
        with open(nome_file, 'r') as file:
            contenuto = file.read()
            numero = int(contenuto)
            risultato = 100 / numero 
            print("Risultato:", risultato)
    except FileNotFoundError:
        print("Il file non è stato trovato")
    except ZeroDivisionError:
        print("Impossibile la divisione per 0")
    except ValueError:
        print("Errore. Valore non convertibile in intero")


