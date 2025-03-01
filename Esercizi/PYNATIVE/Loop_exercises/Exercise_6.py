# Count the total number of digits in a number

numero = int(input("Inserisci un numero: "))

i = 0
while numero != 0:
    numero = numero // 10
    i = i + 1
print(f"Il numero totale delle digitazione è: {i}")