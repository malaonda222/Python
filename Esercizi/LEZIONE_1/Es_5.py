n:int = int(input("Inserisci un numero: "))
is_prime = True

if n<2:
    is_prime = False
else:
    div=2
    while div <= n**0.5:
        if n%div==0:
            is_prime = False 
        else:
            div+=1
    is_prime = False

if is_prime == True:
    print("Il numero è primo")
else:
    print("Il numero non è primo")