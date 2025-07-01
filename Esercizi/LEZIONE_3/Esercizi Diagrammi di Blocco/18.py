# Classifica e somma condizionale

while True:
    n = int(input("Inserisci un numero x: "))
    if n.lstrip("-").isdigit():
        x = int(n)
        break 
    else:
        print("Errore. Inserisci un numero intero.")

i = 0
somma = 0 
media = 0
somma_pari = 0
somma_dispari = 0
valori = []

while i <= n:
    while True:
        x = int(input("Inserisci un valore intero: "))
        if x.lstrip("-").isdigit():
            x = int(x)
            valori.append(x)
            somma += x
            break 
        else:
            print("Errore. Inserisci un numero intero.")

    i += 1

media = somma/i 

for x in valori:
    if x % 2 == 0 and x > media:
        somma_pari += x
    if x < media or x % 2 != 0:
        somma_dispari += x

print(f"La somma dei numeri pari è: {somma_pari}")
print(f"La somma dei numeri dispari è: {somma_dispari}")

if somma_pari > somma_dispari:
    print(f"La somma dei numeri pari ({somma_pari}) è maggiore.")
elif somma_dispari > somma_pari:
    print(f"La somma dei numeri dispari ({somma_dispari}) è maggiore.")
else:
    print("Le somme sono uguali.")