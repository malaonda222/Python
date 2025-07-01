# Find the factorial of a given number
n = int(input("Inserisci un numero intero: "))
fattoriale = 1
if n < 0:
    print("Il fattoriale non esiste per i numeri negativi")
elif n == 0:
    print("Il fattoriale di 0 è 1")
else: 
    for i in range(1, n+1):
        fattoriale *= i
    print(f"Il fattoriale di {n} è {fattoriale}")
