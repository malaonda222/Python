# opzione con ciclo While
# while True:
#     numero = input("Inserisci un numero intero: ")
#     if numero.isdigit() and int(numero) >= 0: 
#         numero = int(numero)
#         break 
#     else:
#         print("Errore. Inserisci un numero intero positivo.")

# fattoriale = 1
# i = 1
# while i <= numero:
#     fattoriale *= i 
#     i = i + 1 
# print(f"Il fattoriale di {numero} è: {fattoriale}.")

# # opzione con ciclo For
# for i in range(1, numero+1):
#     fattoriale *= i
# print(f"Il fattoriale di {numero} è: {fattoriale}.")
'''Il fattoriale di un intero non negativo n, scritto n!, è il prodotto

n * (n-1) * (n-2) * ... * 1

con 1! uguale a 1 e 0! definito come 1.
Si scriva una funzione ricorsiva recursiveFactorial che dato un numero n calcoli n!'''

def recursiveFactorial(numero:int) -> int:
    if numero == 1 or numero == 0:
        return 1
    else: 
        return int(numero * recursiveFactorial(numero-1))
    
print(f"Il fattoriale di 3 è {recursiveFactorial(3)}")
print(f"Il fattoriale di 142 è {recursiveFactorial(142)}")



def recursiveFactorial(numero:int) -> int:
    if numero == 1 or numero == 0:
        return 1
    else:
        return int(numero * recursiveFactorial(numero - 1))