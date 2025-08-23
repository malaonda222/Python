'''Scrivi un programma in Python che:
Chieda all'utente di inserire una lista di numeri interi separati da virgola.
Calcoli e stampi:
Il numero più grande.
Il numero più piccolo.
La media aritmetica.
Quanti numeri sono pari e quanti sono dispari.
La lista dei numeri ordinati in modo crescente e decrescente.'''

def funzione():
    lista_numeri = []
    numeri_pari = 0
    numeri_dispari = 0
    while True:
        valore = input("Inserisci una lista di numeri interi separati da virgole: ")
        if valore == 'stop':
            break 
        try: 
            valore = int(valore)
            lista_numeri.append(valore)
            if valore % 2 == 0:
                numeri_pari += 1
            else:
                numeri_dispari += 1
        except ValueError:
            print("Inserire un numero valido!")
    
    if not lista_numeri:
        return "La lista dei numeri è vuota."
     
    print(f"Numero massimo: {max(lista_numeri)}")
    print(f"Numero minimo: {min(lista_numeri)}")
    media = sum(lista_numeri) / len(lista_numeri)
    print(f"Media: {media}")

    crescente = sorted(lista_numeri)
    decrescente = sorted(lista_numeri, reverse=True)
    print(f"Numeri ordinati in ordine crescente: ", crescente)
    print(f"Numeri ordinati in ordine decrescente: ", decrescente)

    print(f"Numeri pari: {numeri_pari}")
    print(f"Numeri dispari: {numeri_dispari}")

funzione()