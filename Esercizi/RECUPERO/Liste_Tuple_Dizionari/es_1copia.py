def convert_list(lista: list[tuple]) -> dict:
    d: dict = {}
    for key, value in lista:
        if key not in d:
            d[key] = value 
        else:
            d[key] += value 
    return d


def convert(lista1: list[tuple]) -> dict:
    d1: dict = {}
    for element in lista1:
        key, value = element[0], element[1]
        if key not in lista1:
            d1[key] = value 
        else:
            d1[key] += value 
    return d1


l1 = [("ciao", 2), ("come", 3), ("va", 4), ("va", 6)]
print(convert_list(l1))
