# Calcolo del fattoriale di un numero

numero:int = int(input("Inserisci un numero intero e positivo: "))
# if numero < 0:
#     print("Errore. Il numero inserito deve essere positivo.")
# elif numero == 0:
#     print(f"Il fattoriale di {numero} è uguale a 1.")
# else:
#     fattoriale = 1
#     i = 1
#     while True:
#         if i == numero:
#             break
#         else:
#             fattoriale = fattoriale*i
#             i = i + 1
#     print(f"Il fattoriale di {numero} è: {fattoriale}.")

i = 1
fattoriale = 1
if numero < 0:
    print("Errore. Il numero inserito deve essere positivo.")
elif numero == 0:
    print(f"Il fattoriale di {numero} è uguale a 1.")
else:
    for i in range(1, numero + 1):
        fattoriale *= i
    print(f"Il fattoriale di {numero} è: {fattoriale}")