''' Usa map per raddoppiare ogni numero in una lista.'''

def raddoppio(lista: list[int]) -> list[int]:
    return list(map(lambda item: item*2, lista))

print(raddoppio([1, 3, 5, 4, 6, 9]))


def raddoppia(n: int) -> int:
    return n * 2

def raddoppio2(lista: list[int]) -> list[int]:
    return list(map(raddoppia, lista))

print(raddoppio2([1, 6, 5, 777, 7, 3]))