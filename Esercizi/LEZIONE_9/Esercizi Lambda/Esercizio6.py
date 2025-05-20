# Uso con reduce()

from functools import reduce

from typing import Callable

numeri = [2, 3, 4]

prodotto:Callable[[int], int] = reduce((lambda x, y: x * y), numeri)
print(prodotto)


def prodotto(numeri: list[int]) -> int:
    product = 1
    for numero in numeri:
        product *= numero 
    return product

numeri = [2, 3, 4]
print(prodotto(numeri))