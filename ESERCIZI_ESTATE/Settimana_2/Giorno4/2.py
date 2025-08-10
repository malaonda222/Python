'''Usa filter per tenere solo i numeri positivi'''

def num_pos(n: int) -> bool:
    return n > 0

def numeri_positivi(lista: list[int]) -> list[int]:
    return list(filter(num_pos, lista))

def numeri_positivi2(lista: list[int]) -> list[int]:
    return list(filter(lambda item: item > 0, lista))

print(numeri_positivi([9, 4, 6, 3, 66, 7, 4, -9, -8, -3]))