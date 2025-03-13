'''Scelta condizionata basata su input multipli'''
n = int(input("Inserisci un numero a piacere: "))
i = 0

# for i in range(n+1):
#     x = int(input("Inserisci il valore di x: "))
#     y = int(input("Inserisci il valore di y: "))
#     if x > 0 and y > 0:
#         result = x*y
#         print(f"Il prodotto di {x} e {y} è: {result}")
#         i = i + 1
#     else:
#         if x < 0 and y < 0:
#             print("Errore.")
#             i = i + 1
#         else:
#             result = x+y
#             print(f"La somma di {x} e {y} è: {result}")
#             i = i + 1

while i <= n:
    x = int(input("Inserisci il valore di x: "))
    y = int(input("Inserisci il valore di y: "))
    if x > 0 and y > 0:
        result = x*y
        print(f"Il prodotto di {x} e {y} è: {result}")
        i = i + 1
    else:
        if x < 0 and y < 0:
            print("Errore.")
            i = i + 1
        else:
            result = x+y
            print(f"La somma di {x} e {y} è: {result}")
            i = i + 1



         
