'''Crea un gestore personalizzato per file non trovati.'''

def gestore_personalizzato(file_name):
    try:
        with open(file_name, 'r') as file:
            contenuto = file.read()
            return contenuto
    except FileNotFoundError:
        raise ValueError("Il file non esiste")

    
print(gestore_personalizzato(file_name="file_che_non_esiste.txt"))