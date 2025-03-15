# Calcolo di sequenze condizionali
while True:
    n = float(input("Inserisci un numero positivo: "))
    if n % 1 == 0:
        break
    print("Errore: Il numero deve essere positivo.")

if n > 0:
    if n % 2 == 0:
        cont = 4 
        result = 0 
        while cont <= n:
            result = result + cont 
            cont = cont + 4 
        print(f"Il risultato è della sequenza condizionale è: {result}.")

    else:
        cont = 1
        result = 1
        while cont <= n:
            result = result * cont 
            cont = cont + 2
        print(f"Il risultato della sequenza condizionale è: {result}.")

else:
    print("Errore. Il numero n deve essere positivo.")