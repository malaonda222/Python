'''Scrivi una funzione calcolatrice(a, b, operazione) che:
    Riceve due numeri a e b, e una stringa operazione che può essere "add", 
    "sub", "mul" o "div".
    In base all’operazione, restituisce il risultato dell’operazione 
    tra a e b.
    Gestisci il caso di divisione per zero con un messaggio di errore'''


def calcolatrice():
    a: float = float(input("Inserisci il primo numero: "))
    b: float = float(input("Inserisci il secondo numero: "))
    operazione: str = input("Inserisci l'operazione (scelta tra 'add', 'sub', 'mul', 'div'): ")
    
    match operazione:
        case "add":
            return f"Il risultato dell'addizione è: {a + b}"  
        case "sub":
            return f"Il risultato della sottrazione è: {a - b}" 
        case "mul":
            return f"Il risultato della moltiplicazione è: {a * b}" 
        case "div":
            if b == 0:
                raise ValueError
            return f"Il risultato della divisione è: {(a / b):.2f}" 
        case _:
            return "Errore. Operazione non riconosciuta"
            
# print(calcolatrice(1, 5, "add"))
# print(calcolatrice(1, 6, "sub"))
# print(calcolatrice(3, 8, "mul"))
# print(calcolatrice(18, 0, "div"))

print(calcolatrice())
