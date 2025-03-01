# Print multiplication table of a given number

n = int(input("Inserisci un numero: "))
product = 1
for x in range (1, 11, 1):
    product = n*x
    print(product)

i = 1
numero = int(input("Inserisci un numero: "))
while i <= 10:
    prodotto = numero*i
    i+=1
    print(prodotto)