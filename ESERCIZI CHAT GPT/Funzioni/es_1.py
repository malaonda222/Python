def somma_pari():
     numeri = input("Inserisci una lista di numeri separati da spazi: ")
     lista_numeri = [int(num) for num in numeri.split()]
     somma = 0
     for i in lista_numeri:
        if i % 2 == 0:
            somma += i 
     return somma 

somma = somma_pari()
print(f"La somma dei numeri pari è: {somma}")


def conta_dispari(lista:list):
    dispari = 0 
    
    for x in lista:
        if x % 2 != 0:
            dispari += 1
    return dispari 

odd = [1, 8, 4, 66, 53, 59]
dispari = conta_dispari(odd)
print(f"I numeri dispari della lista sono: {dispari}")