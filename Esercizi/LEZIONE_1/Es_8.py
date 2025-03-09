# Trovare i numeri maggiori di un valore soglia
soglia:float = float(input("Inserisci un valore soglia: "))
cont = 0

while cont < 7:
    n:float = float(input("Inserisci un numero: "))
    if n > soglia:
        print(f"Il valore {n} è maggiore della soglia.")
    cont = cont + 1

for i in range(7):
    n:float = float(input("Inserisci un numero: "))
    if n > soglia:
        print(f"Il valore {n} è maggiore della soglia.")
