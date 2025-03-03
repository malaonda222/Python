n:int = int(input("Inserisci un numero: "))
primo = True

while True:
    if n<2:
        primo = False
    else:
        div=2
        if div<n:
            if n%div==0:
                prime = True
            else:
                div+=1
        else:
            prime = False 
        
            if primo == True:
                print("Il numero è primo")
            else:
                print("Il numero non è primo")