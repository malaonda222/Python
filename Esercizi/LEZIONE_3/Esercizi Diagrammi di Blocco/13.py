'''Esercizi di controllo numerico con condizioni arbitrarie'''
# while True:
#     x = int(input("Inserisci un valore per \"x\": "))   
#     y = int(input("Inserisci un valore per \"y\": "))
#     z = int(input("Inserisci un valore per \"z\": "))
#     if x%1 == 0 and x > 0:
#         if y % 1 == 0 and y > 0:
#             if z % 1 == 0 and z > 0:
#                 if (x+y+z) % 2 == 0 and x % 3 == 0 and y % 5 == 0 and z % 7 == 0:
#                     print("Regole rispettate.")
#                     break
#                 else: 
#                     print("Regole non rispettate.")
#             else:
#                 print("z deve essere intero positivo.")
#         else:
#             print("y deve essere intero e positivo.")
#     else:
#         print("x deve essere intero e positivo.")


def verifica_regole(x:int, y:int, z:int):
    if (x+y+z) % 2 == 0:
        if x % 3 == 0 and y % 5 == 0 and z % 7 == 0:
            print("Regole rispettate.")
                    
        else: 
            print("Regole non rispettate.")
    else:
        print("Regole non rispettate.")

verifica_regole(6, 10, 14)
