punteggio = 0
while punteggio < 100: 
    d1 = int(input("Inserisci il risultato del primo dado: "))
    d2 = int(input("Inserisci il risultato del secondo dato: "))
    
    if d1 > 0 and d1 <= 6 and d2 > 0 and d2 <= 6:
        somma = d1 + d2
        if d1%2 == 0 and d2%2 == 0 and somma > 8:
            punteggio = 100
        elif d1 == 6 or d2 == 6 or somma == 7:
            punteggio += 10
        else:
            punteggio = 0
            print("Sconfitta!")
    
    else:
        print("Errore. Ritirare i dadi.")
        continue 
else:
    print("Vittoria!")