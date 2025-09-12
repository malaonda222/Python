def calcolatrice():
    try:
        a = int(input("Inserisci il primo numero: "))
        b = int(input("Inserisci il secondo numero: "))
    except ValueError:
        return "Gli input devono numeri interi"
    
    operazione = input("Inserisci l'operazione (+, -, *, /): ")
    try: 
        if operazione == "+":
            return f"Somma: {a+b}"
        elif operazione == "-":
            return f"Sottrazione: {a-b}"
        elif operazione == "*":
            return f"Moltiplicazione: {a*b}"
        elif operazione == "/":
            return f"Divisione: {a/b}"
        else:
            return "Operatore non valido"
    except ZeroDivisionError:
        return "Errore. Impossibile dividere per 0"
    except ValueError as e:
        return f"Errore: {e}"


print(calcolatrice())