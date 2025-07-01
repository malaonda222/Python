'''Determinare la somma dei numeri dentro un intervallo'''
a = int(input("Inserisci un valore per \"a\": "))
b = int(input("Inserisci un valore per \"b\": "))

if a < b:
    if a > 0 and b > 0:
        if a % 1 == 0 and b % 1 == 0:
            sum = 0
            i = a 
            for i in range(a, b+1):
                sum = sum + i
                i = i + 1

        else:
            print("A e B devono essere positivi.")
    else:
        print("A e B devono essere positivi.")                        
else: 
    print("A deve essere minore di B.")

print(f"La somma di tutti i numeri interi compresi tra {a} e {b} è: {sum}")
