# Somma condizionata di numeri in base a un valore x
x = int(input("Inserisci un valore positivo x: "))
if x > 0:
    i = 0
    sum = 0
    while i != 10:
        n = int(input("Inserisci un valore n: "))
        if x%2 == 0:
            if n > x/2:
                sum = sum + n
                i = i + 1
            else:
                i = i + 1
        elif x%2 != 0:
            if n < x:
                sum = sum + n 
                i = i + 1
            else:
                i = i + 1
    else:
        print(f"La somma condizionata di numeri in base al valore {x} è: {sum}")

elif x < 0:
    print("Errore. Il numero x deve essere positivo.")

    