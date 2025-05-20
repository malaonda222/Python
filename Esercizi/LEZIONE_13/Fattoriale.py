# Calcolo fattoriale

# opzione con ciclo
# while True:
#     n = input("Inserisci un numero intero e positivo: ")
#     if n.isdigit() and int(n) >= 0:
#         n = int(n)
#         break
#     else:
#         print("Inserisci un numero intero e positivo.")
        
# if n == 0:
#     print(1)

# else: 
#     fattoriale = 1
#     for i in range(1, n + 1):
#         fattoriale *= i 
#     print(f"Il fattoriale è {fattoriale}.")


# opzione con funzione ricorsiva
def fattoriale(numero:int) -> None:
    if numero == 0:
        return 1
    if numero < 0:
        print("Errore.")
    else:
        return (numero * fattoriale(numero - 1))
    
print(fattoriale(5))
print(fattoriale(4))



