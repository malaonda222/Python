# Print the Sum of a Current Number and a Previous number

somma = 0
numero_precedente = 0
for x in range(10):
    somma = numero_precedente+1
    print(f"Current number: {x}; Previous Number: {numero_precedente}; Sum: {somma}")
    numero_precedente+=x