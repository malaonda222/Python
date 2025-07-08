def somma_indici_pari(lista: list):
    somma = 0
    for i in range(len(lista)):
        if i % 2 == 0:
            somma += lista[i]
    return somma

print(somma_indici_pari([5, 8, 12, 7, 3, 10]))