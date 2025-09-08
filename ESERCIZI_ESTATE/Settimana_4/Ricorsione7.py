def somma_nidificata(lista: list) -> int:
    if len(lista) == 0:
        return 0
    
    x = lista[0]
    resto = lista[1:]

    if isinstance(x, list):
        return somma_nidificata(x) + somma_nidificata(resto)
    else:
        return x + somma_nidificata(resto)


print(somma_nidificata([1, [2, [3, 4], 5], 6]))
print(somma_nidificata([[1], [2, [3]], 4]))
print(somma_nidificata([]))