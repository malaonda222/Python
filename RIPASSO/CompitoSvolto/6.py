'''Scrivere un programma che acquisisca in input due numeri interi, n1 e n2, e calcoli il prodotto di tutti 
i numeri compresi tra n1 e n2, inclusi gli estremi.
Il programma deve gestire anche il caso in cui n1 > n2, calcolando comunque il prodotto correttamente.'''

numero_1: int = int(input("Inserisci il primo numero intero: "))
numero_2: int = int(input("Inserisci il secondo numero intero: "))
prodotto = 1

if numero_1 % 1 != 0 or numero_2 % 1 != 0:
    raise ValueError("Entrambi i numeri devono essere interi!")
if numero_1 > numero_2: 
    for i in range(numero_2, numero_1 + 1):
        prodotto *= i 
    print(f"Il prodotto è: {prodotto}")
else:
    for i in range(numero_1, numero_2 + 1):
        prodotto *= i 
    print(f"Il prodotto è: {prodotto}")

