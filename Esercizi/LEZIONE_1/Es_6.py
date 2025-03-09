# Calcolo del fattoriale di un numero

numero:int = int(input("Inserisci un numero intero e positivo: "))
if numero%1 != 0 and numero<0:
    print("Errore. Il numero inserito deve essere intero e positivo.")
else:
    fattoriale = 1
    i = 1
    while i <= numero:
        fattoriale = fattoriale*i
        i = i + 1
    print(f"Il fattoriale di {numero} è: {fattoriale}.")


while True:
    numero:int = int(input("Inserisci un numero intero e positivo: "))
    if numero>0:
        break
    print("Errore. Il numero deve essere positivo.")
fattoriale = 1
for i in range(1, numero + 1):
    fattoriale *= i
print(f"Il fattoriale di {n} è: {fattoriale}")