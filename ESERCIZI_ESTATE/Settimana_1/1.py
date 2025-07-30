''' Scrivi una funzione che somma tutti gli elementi di una lista.'''


def somma_elementi() -> int:
    somma_numeri = 0
    while True:
        valore = input("Inserisci un numero: ")
        if valore.lower() == "stop":
            break 
        try:
            valore = int(valore)
            somma_numeri += valore 
        except ValueError:
            print("Inserire un numero intero!")
    print(f"La somma dei numeri è: {somma_numeri}")

somma_elementi()
