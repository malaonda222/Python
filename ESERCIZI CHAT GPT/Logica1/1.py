'''Pari o dispari
Scrivi un programma che chiede un numero all’utente e dice se è pari o dispari.'''

def pari_dispari() -> None:
    numero = input("Inserisci un numero: ")
    try:
        numero = int(numero)
        if numero <= 0:
            print("Il valore deve essere un numero intero maggiore di zero.")
            return            
    except ValueError:
        print("Inserisci un numero valido.")
        return 
    print(f"Il numero inserito è: {numero}")

    if numero % 2 == 0:
        print(f"Numero {numero} pari!")
    else:
        print(f"Numero {numero} dispari!")

pari_dispari()