def validazione_numero(num: float) -> bool:
    if num.is_integer() and num > 0:
        return True
    else:
        return False 

while True:
    x = float(input("Inserisci un numero intero positivo: "))
    if validazione_numero(x) == True:
        break
print(f"Il numero scelto è: {int(x)}")


sequenza_numeri = []
while True:
    numero = float(input("Inserisci un numero: "))
    if numero == 0:
        break 
    if validazione_numero(numero) == True:
        sequenza_numeri.append(int(numero))
    else:
        continue
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