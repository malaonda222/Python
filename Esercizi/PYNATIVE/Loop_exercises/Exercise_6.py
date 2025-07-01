# Count the total number of digits in a number

numero = 748569
cont = 0

while numero != 0:
    numero = numero // 10
    cont = cont + 1
print(cont)


