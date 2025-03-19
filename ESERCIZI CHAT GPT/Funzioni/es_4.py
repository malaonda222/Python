# Calcolatrice con funzioni

def somma(a:int, b: int): 
    return a + b

def sottrazione(a:int, b:int):
    return a - b

def moltiplicazione(a:int, b:int):
    return a * b

def divisione(a:int, b:int):
    if b == 0:
        print("Errore: divisione per 0")
    return a / b


def calcolatrice():
    print("Scegli un'opzione: ")
    print("1. Somma")
    print("2. Sottrazione")
    print("3. Moltiplicazione")
    print("4. Divisione")

    scelta = input("Inserisci il numero dell'operazione (1/2/3/4): ")

    if scelta not in [1, 2, 3, 4]:
        print("Operazione non valida!")
        return 
    
    num1 = float(input("Inserisci il primo numero: "))
    num2 = float(input("Inserisci il secondo numero: "))

    if scelta == '1':
        print(f"Il risultato è: {somma(num1, num2)}")
    elif scelta == '2':
        print(f"Il risultato è: {sottrazione(num1, num2)}")
    elif scelta == '3':
        print(f"Il risultato è: {moltiplicazione(num1, num2)}")
    elif scelta == '4':
        print(f"Il risultato è: {divisione(num1, num2)}")

calcolatrice()
    