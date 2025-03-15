while True:
    n = input("Inserisci un numero intero n: ")

    if n.lstrip('-').isdigit(): #lstrip leva il segno negativo qualora ci sia, isdigit controlla che siano solo numeri
        n = int(n)
        break
    else:
        print("Inserisci un numero intero.")

if n > 0 and n <= 100:
    somma = 0
    i = 1
    while i <= n:
        if i % 2 == 0:
            somma += i
            i = i + 1
        else:
            i = i + 1
        print(f"La somma è: {somma}")
            
if n == 0 or n < 0: 
    print("Errore.")

else:
    somma = 0
    i = 1
    while i <= n:
        if i % 2 != 0:
            somma += i
            i = i + 1 
        else:
            i = i + 1
    print(f"La somma è: {somma}")
