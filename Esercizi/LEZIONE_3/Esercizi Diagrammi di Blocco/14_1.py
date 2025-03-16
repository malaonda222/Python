# Simulazione di un gioco di dati
punteggio = 0

while True:
    while True:
        d1 = input("Inserisci il valore del primo dado: ")
        d2 = input("Inserisci il valore del secondo: ")
        if d1.lstrip('-').isdigit() and d2.lstrip('-').isdigit():
            d1 = int(d1)
            d2 = int(d2)
            break
        else:
            print("Inserisci un numero intero.")
        
        if d1 > 0 and d1 <= 6 and d2 > 0 and d2 <= 6:
                break
        print("Errore. I valori dei dadi devono essere tra 1 e 6.")

    somma = d1 + d2

    if d1 % 2 == 0 and d2 % 2 == 0 and somma > 8:
        punteggio = 100
    elif d1 == 6 or d2 == 6 or somma == 7:
        punteggio += 10
    else:
        punteggio = 0

    if punteggio >= 100 or punteggio == 0:
        break

if punteggio >= 100:
    print("Vittoria!")
else:
    print("Sconfitta!")