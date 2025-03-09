# Conta i numeri pari e dispari
pari = 0
dispari = 0
cont = 0

while cont < 10:
    n:float = float(input("Inserisci un numero: "))
    if n%2 == 0:
        pari = pari + 1 
    else:
        dispari = dispari + 1
    cont = cont + 1

print(f"I numeri pari sono: {pari}")
print(f"I numeri dispari sono: {dispari}")


for cont in range(10):
    n:int = int(input("Inserisci un numero: "))
    if n%2 == 0:
        pari = pari + 1 
    else:
        dispari = dispari + 1

print(f"I numeri pari sono: {pari}")
print(f"I numeri dispari sono: {dispari}")
