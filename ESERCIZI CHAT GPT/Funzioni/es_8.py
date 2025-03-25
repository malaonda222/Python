def esegui_operazioni(a:int, b:int, operazione:str):
    if operazione == "1":
        return a + b
    elif operazione == "2":
        return a + b
    elif operazione == "3":
        return a * b
    elif operazione == "4":
        if b == 0:
            return "Errore. Divisione per zero."
        else:
            return a / b
    else:
        return "Operazione non valida."

def main():
    a = int(input("Inserisci il primo numero: "))
    b = int(input("Inserisci il secondo numero: "))

    print("Scegli un'opzione tra le seguenti: \n")
    print("1 - Somma")
    print("2 - Sottrazione")
    print("3 - Moltiplicazione")
    print("4 - Divisione")

    scelta = int(input("Inserisci il numero dell'operazione (somma, sottraizone, moltiplicazione, divisione: "))
    risultato = esegui_operazioni(a, b, scelta)
    print(f"Il risultato dell'operazione è: {risultato}.")

main()