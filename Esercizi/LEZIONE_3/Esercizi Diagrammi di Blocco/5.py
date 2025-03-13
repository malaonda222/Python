'''Calcolo della somma dei quadrati fino a un numero intero positivo n'''
n = int(input("Inserisci un numero n: "))

if n%1 == 0 and n>0:
    sum = 0
    i = 1
    while i < n:
        for i in range(n+1): 
            sum = sum + (i*i)
            i = i + 1
    else:
        print(f"La somma dei quadrati del numero {n} è: {sum}")
else:
    print("Errore. Il numero inserito deve essere positivo.")
    

