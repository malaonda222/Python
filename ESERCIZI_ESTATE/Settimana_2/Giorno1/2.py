'''Crea una funzione che calcola la media di una lista.'''

def media_lista() -> float:
    lista_numeri: list = []
    while True:
        valore = input("Inserisci un numero intero maggiore di zero: ")
        if valore.lower() == "fine":
            break 
        try: 
            valore = int(valore)
            if valore <= 0:
                print("Errore. Il numero deve essere maggiore di zero!")
            else:
                lista_numeri.append(valore)
        except ValueError:
            print("Errore! Prego inserire un numero valido.")
    print(lista_numeri)

    somma_numeri = sum(lista_numeri)
    if not somma_numeri:
        print("Lista dei numeri vuota")
    else:
        media_numeri = somma_numeri/len(lista_numeri)
        print(f"La media dei numeri inseriti è: {media_numeri:.2f}")

media_lista()