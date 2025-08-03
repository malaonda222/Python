'''Trova il massimo e minimo in una lista'''

lista_numeri = []
while True:
    valore = input("Inserisci un numero intero: ")
    if valore.lower() == "fine":
        break 
    try: 
        valore = int(valore)
        lista_numeri.append(valore)
    except ValueError:
        print(f"Errore. Il numero deve essere intero!")

print(lista_numeri)

print(f"Il numero più piccolo della lista è: {min(num for num in lista_numeri)}")
print(f"Il numero più grande della lista è: {max(num for num in lista_numeri)}")

minimo = lista_numeri[0]
massimo = lista_numeri[0]
for element in lista_numeri:
    if element > massimo:
        massimo = element 
    if element < minimo:
        minimo = element 
print(f"{minimo}, {massimo}")
