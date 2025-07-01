# Filtrare e classificare i numeri
dispari = 0
pari = 0
negativi = 0
positivi = 0
i = 0

while i < 10:
        n = float(input("Inserisci un numero intero: "))
        if n % 1 == 0 and n != 0:
            if n > 0:
                positivi += 1
                if n % 2 == 0 and n > 20: 
                    pari += 1
                    i = i + 1 
                else:
                    i = i + 1
        
            else:
                negativi += 1
                if n % 2 != 0 or n < -10:
                    dispari += 1
                    i = i + 1
                else:
                    i = i + 1

        else:
            print("Errore. Inserisci un numero intero.")
            continue 

print(f"I numeri positivi sono: {positivi}")
print(f"I numeri negativi sono: {negativi}")
print(f"I numeri pari sono: {pari}")
print(f"I numeri dispari sono: {dispari}")
