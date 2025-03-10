#Verifica se un numero è primo
n:int = int(input("Inserisci un numero: "))
numero_primo = True

if n<0:
    print(f"{n} non è un numero intero positivo")
else:
    if n < 2:
        numero_primo = False 
    else:
        for i in range(2, n):
              if n%i == 0: #serve per capire se il numero è primo o no
                  numero_primo = False
                  break
    if numero_primo:
        print(f"{n} è un numero primo")
    else:
        print(f"{n} non è un numero primo")
        

# import math
# #se il numero è minore di 2, non è primo
# if n < 2: 
#      is_prime = False
# else:
#      div = 2 #inizializza il divisore
#      limit = math.sqrt(n) #limite superiore della ricerca dei divisori (radice quadrata di n)

#      while div <= limit: #controlla solo fino a radice quadrata di n
#           if n%div == 0:
#                is_prime = False #se trova un divisore, il numero non è primo
#                break
#           div += 1 #incrementa il divisore

# if is_prime:
#      print("Il numero è primo.")
# else:
#      print("Il numero non è primo.")