def trova_duplicati(lista_numeri: list[int]) -> set[int]:
    numeri_duplicati = set()
    for numero in lista_numeri:
        if lista_numeri.count(numero) >= 2:
            numeri_duplicati.add(numero)
    return numeri_duplicati


def trova_duplicati2(lista_numeri: list[int]) -> set[int]:
    visti = set()
    duplicati = set()
    for numero in lista_numeri:
        if numero in visti:
            duplicati.add(numero)
        else:
            visti.add(numero)
    return duplicati

print(trova_duplicati([1, 2, 3, 2, 4, 5, 1, 6]))
print(trova_duplicati2([1, 2, 3, 2, 4, 5, 1, 6]))
