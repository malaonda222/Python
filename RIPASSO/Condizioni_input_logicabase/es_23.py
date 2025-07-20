'''Scrivi una funzione remove_duplicates(lst) che riceve una lista e ritorna 
una nuova lista senza duplicati, mantenendo l’ordine originale.'''

def crea_lista() -> list: 
    lst: list = []
    while True:
        input_utente = input("Inserici un numero maggiore positivo: ")
        if input_utente.lower() == "fine":
            break
        try: 
            input_utente = int(input_utente)
            if input_utente <= 0:
                print("Inserisci un numero intero, stringa o numero negativo non supportati")
                continue
            else:
                lst.append(int(input_utente))
        except ValueError:
            print("Errore. L'input deve essere un numero intero maggiore di 0!")
    return lst
    


def remove_duplicates() -> list:
    lst: list = crea_lista()
    new_list = []
    for element in lst:
        if element not in new_list:
            new_list.append(element) 
    print(f"Nuova lista senza duplicati; {new_list}")

    

remove_duplicates()
