# Classifica e somma condizionale
while True:
    n = int(input("Inserisci un numero n: "))
    if n < 0:
        print("Errore. Inserisci un numero intero.")
        continue
    else:
        i = 1
        somma = 0 
        media = 0
        somma_pari = 0
        somma_dispari = 0

        while i <= n:
            x = int(input("Inserisci un numero x: "))
            if x % 1 != 0:
                print("Errore. Inserisci un numero intero.")
                continue 
            else:
                somma += x
                media = somma/i 
                if x % 2 == 0 and x > media:
                    somma_pari += x 
                    i = i + 1
                if x < media or x % 2 != 0:
                    somma_dispari += x
                    i = i + 1

        print(f"La somma dei numeri pari è: {somma_pari}")
        print(f"La somma dei numeri dispari è: {somma_dispari}")

        if somma_pari > somma_dispari:
            print(f"La somma dei numeri pari ({somma_pari}) è maggiore.")
        elif somma_dispari > somma_pari:
            print(f"La somma dei numeri dispari ({somma_dispari}) è maggiore.")
        else:
            print("Le somme sono uguali.")