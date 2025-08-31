def somma_posizione_pari(lista_numeri: list[int]) -> int:
    somma_elementi = 0
    for i in range(len(lista_numeri)):
        if i % 2 == 0:
            somma_elementi += lista_numeri[i]
    return somma_elementi


def somma_posizione_pari2(lista_numeri: list[int]) -> int:
    somma_elementi = 0
    for i in range(0, len(lista_numeri), 2):
        somma_elementi += lista_numeri[i]
    return somma_elementi

def somma_posizione_pari3(lista_numeri: list[int]) -> int:
    return sum(lista_numeri[::2])

print(somma_posizione_pari([10, 20, 30, 40, 50]))
print(somma_posizione_pari2([10, 20, 30, 40, 50]))
print(somma_posizione_pari3([10, 20, 30, 40, 50]))

    