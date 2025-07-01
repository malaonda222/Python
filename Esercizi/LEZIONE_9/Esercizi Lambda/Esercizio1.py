# Sintassi

from typing import Callable

quadrato: Callable[[int], int] = lambda x: x ** 2
print(quadrato(10))


def quadrato(x:int) -> int:
    return x ** 2

