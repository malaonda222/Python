def somma(lista: list) -> int:
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + somma(lista[1:])

print(somma([1, 2, 3, 4]))