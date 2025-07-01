# esercizio con opzione while

#legge il primo valore
max:float = float(input("Inserisci un numero: "))
i = 1
while i<=3:
    i+=1
    n:float = float(input("Inserisci un numero: "))
    if n>max: #controlla
        max = n

print(f"Il numero massimo è: {max}")


# esercizio con opzione for

#legge il primo valore
massimo:float = float(input("Inserisci un numero: "))

for i in range(3): #il ciclo si ripete 3 volte
    numero:float = float(input("Inserisci un numero: ")) #legge il primo numero
    if numero > massimo: #controlla se è maggiore
        massimo = numero
print(f"Il numero massimo è {massimo}")


# esercizio con opzione repeat until

#legge il primo valore
max1:float = float(input("Inserisci il primo numero: "))
i = 1

while True:
    num:float = float(input("Inserisci un numero: ")) #legge il numero
    if n>max1: #controlla se è maggiore
        max1=num
    i+=1 #incrementa contatore
    if i==4: #condizione di uscita
        break 
print(f"Il massimo valore è: {max1}")
