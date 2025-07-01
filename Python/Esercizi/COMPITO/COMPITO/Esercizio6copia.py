'''Scrivere un programma che acquisisca in input due numeri interi, n1 e n2, e calcoli il prodotto di tutti 
i numeri compresi tra n1 e n2, inclusi gli estremi.
Il programma deve gestire anche il caso in cui n1 > n2, calcolando comunque il prodotto correttamente.'''

while True: 
    n1 = input("Inserisci il primo numero intero \"n1\": ")
    if n1.lstrip('-').isdigit():
        n1 = int(n1)
        break
    else:
        print("Errore. Inserisci un numero intero \"n2\": ")

while True: 
    n2 = input("Inserisci il secondo numero intero: ")
    if n2.lstrip('-').isdigit():
        n2 = int(n2)
        break
    else:
        print("Errore. Inserisci un numero intero.")

# caso in cui n1 > n2
if n1 > n2:
    for i in range(n2, n1+1):
        product *= i

# caso in cui n1 < n2
elif n1 < n2 :
    for i in range(n1, n2+1):
        product *= i
        
# caso in cui n1 = n2
else :
    product = n1

# mostra in output il risultato
print(f"Prodotto: {product}")



# oppure 
temp = 0
if n1 > n2: 
    temp = n1 
    n1 = n2 
    n2 = temp 
prodotto = 1
for x in range (n1, n2 + 1):
    prodotto *= x
else:
    product = n1

print(f"Il prodotto dei numeri compresi tra n1 e n2 è {prodotto}.")

    
    
    
    
    
    
    