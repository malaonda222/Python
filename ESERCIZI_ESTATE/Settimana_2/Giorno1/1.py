'''Scrivi una funzione che calcola il fattoriale.'''

def fattoriale() -> int:
    while True:
        n = input("Inserisci il numero: ")
        try: 
            n = int(n)
            if n < 0:
                print("Errore, il numero deve essere positivo")
            else:
                print(f"Numero scelto: {n}")
                break
        except ValueError:
            print("Inserisci un valore valido")

    i = 1
    fattoriale = 1
    while i <= n:
        fattoriale *= i
        i += 1 
    print(f"Fattoriale di {n}: {fattoriale}")

fattoriale()

numero: int = 4
fatt = 1
for i in range(1, numero + 1):
    fatt *= i 
print(f"Il fattoriale di {numero} è: {fatt}") 


def rec_fact(num: int) -> int:
    if num < 0:
        return 0
    if num == 0 or num == 1:
        return 1
    else:
        return num * rec_fact(num - 1)
    
print(rec_fact(5))

