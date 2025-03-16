def conta_pari():

    while True:
        lista_numeri = []
        inp = int(input(f"Inserisci un numero (oppure digita \"fine\" per terminare): "))
        while inp != "fine":
            lista_numeri.append(inp)
            print(lista_numeri)
        else:
            break

    for numero in lista_numeri:  
        count_pari = 0
        if numero % 2 == 0:
            count_pari += 1
        return count_pari


pari = conta_pari()
print(f"I numeri pari della lista inserita sono: {pari}")
