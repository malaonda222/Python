'''Conteggio dei numeri divisibili'''

# n = int(input("Inserisci un numero n: ")) #chiedere all'utente di inserire un valore n
# if n < 0: #se il numero è negativo, il programma si interrompe
#     print("Il numero deve essere positivo.")
# else:
#     if n % 1 != 0: #verifica se il numero è intero 
#         print("Il numero deve essere intero positivo.")
#     else:
#         cont = 0
#         i = 0
#         while i != 10: #imposta il ciclo while in modo che l'utente possa inserire 10 x
#             x = int(input("Inserisci un valore per x: "))
#             if x % n == 0: #condizione per verificare che x sia divisibili per n
#                 cont = cont + 1
#                 i = i + 1
#             else:
#                 i = i + 1
#         print(f"Il risultato del conteggio: {cont}") #stampa il risultato

n = int(input("Inserisci un numero n: ")) #chiedere all'utente di inserire un valore n
if n < 0: #se il numero è negativo, il programma si interrompe
    print("Il numero deve essere positivo.")
else:
    if n % 1 != 0: #verifica se il numero è intero 
        print("Il numero deve essere intero positivo.")
    else:
        cont = 0
        i = 0
        for i in range(10):
            x = int(input("Inserisci un valore per x: "))
            if x % n == 0: #condizione per verificare che x sia divisibili per n
                cont = cont + 1
                i = i + 1
            else:
                i = i + 1
        print(f"Il risultato del conteggio: {cont}")
