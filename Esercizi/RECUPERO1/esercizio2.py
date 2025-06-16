while True:
    x = float(input("Inserisci un numero intero positivo: "))
    if x.is_integer() and x > 0:
        print(f"Il numero scelto è: {int(x)}")
        break
    else:
        print("Errore. Il numero deve essere un intero positivo") 

sequenza_numeri = []
while True:
    numero = float(input("Inserisci un numero: "))
    if numero == 0:
        break
    if numero.is_integer() and numero > 0:
        sequenza_numeri.append(int(numero))
        continue
    else:
        print("Errore. Il numero deve essere intero e positivo")
print(f"Sequenza di numeri: {sequenza_numeri}")

occorrenze = 0
for element in sequenza_numeri:
    if element == x:
        occorrenze += 1
print(f"Numero di occorrenze del numero scelto: {occorrenze}")


if x in sequenza_numeri:
    posizione = sequenza_numeri.index(x)
    print(f"Il numero si ripete nella seguente posizione: {posizione}")
else:
    print("Il numero non si ripete")

somma_valori = 0
for element in sequenza_numeri:
    if element == x:
        continue 
    else:
        somma_valori += element 
print(f"Somma dei valori diversi da x: {somma_valori}")