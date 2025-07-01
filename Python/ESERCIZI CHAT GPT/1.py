# Controllare se un numero è positivo, negativo o zero

numero:float = float(input("Inserisci un numero: "))

# match statement
match numero:
    case numero if numero > 0:
        print(f"Il numero è positivo.")
    case numero if numero < 0:
        print(f"Il numero è negativo.")
    case 0:
        print(f"Il numero è pari a 0")