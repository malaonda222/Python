'''Logica: Trova l’unico elemento non duplicato in una lista dove tutti gli altri appaiono due volte.'''

def elemento_unico(lista1: list[int|str|bool|float]) -> list:
    lista_non_duplicati = []
    for element in lista1:
        if lista1.count(element) == 1:
            lista_non_duplicati.append(element)
    return lista_non_duplicati

lista1: list = (1, 4, "ciao", "fine", 5, 7, 1, 4, "fine", 5, 7)

print(elemento_unico(lista1))


def unico(lista2: list[int|str|bool|float]) -> list:
    lista_non_duplicati = []
    for elemento in lista2:
        if elemento not in lista_non_duplicati:
            lista_non_duplicati.append(elemento)
    return lista_non_duplicati

lista2: list = (1, 4, "ciao", "fine", 5, 7, 1, 4, "fine", 5, 7)
print(unico(lista2))

numero = 2**128 
print(len(numero))
