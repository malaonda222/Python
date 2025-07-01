'''Esercizi di controllo numerico con condizioni arbitrarie'''
while True:
    x = input("Inserisci un valore per \"x\": ")
    while True:
        if x.lstrip('-').isdigit() and int(x) > 0:
            x = int(x)
            break
        else:
            print("x deve essere intero positivo.")

    y = int(input("Inserisci un valore per \"y\": "))
    while True:
        if y.lstrip('-').isdigit() and int(y) > 0:
            y = int(y)
            break
        else:
            print("y deve essere intero positivo.")

    z = int(input("Inserisci un valore per \"z\": "))
    while True:
        if z.lstrip('-').isdigit() and int(z) > 0:
            z = int(z)
            break
        else:
            print("z deve essere intero positivo.")

    if (x+y+z) % 2 == 0 and x % 3 == 0 and y % 5 == 0 and z % 7 == 0:
        print("Regole rispettate.")
                    
else: 
    print("Regole non rispettate.")
    

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
#                     continue
#             else:
#                 print("z deve essere intero positivo.")
#                 continue
#         else:
#             print("y deve essere intero e positivo.")
#             continue
#     else:
#         print("x deve essere intero e positivo.")


def verifica_regole(variabile:int):
    while True:
        valore = input(f"Inserire un valore \"{variabile}\" intero e positivo.")

        if valore.isdigit() and int(valore) <= 0:
            valore = int(valore)
            return valore
        
        else:
            print(f"Errore. Il numero deve essere intero e positivo.")

if (x+y+z) % 2 == 0 and x % 3 == 0 and y % 5 == 0 and z % 7 == 0:
        print("Regole rispettate.")
                    
else: 
    print("Regole non rispettate.")

verifica_regole(6, 10, 14)
