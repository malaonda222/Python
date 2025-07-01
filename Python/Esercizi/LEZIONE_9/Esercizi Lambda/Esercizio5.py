# Funzione lambda con if

from typing import Callable

numero_pari_dispari:Callable[[int], int] = lambda x: "Pari" if x % 2 == 0 else "Dispari"
print(numero_pari_dispari(8))
print(numero_pari_dispari(9))


def pari_dispari(x:int) -> int:
    if x % 2 == 0:
        return "Pari"
    else:
        return "Dispari"

print(pari_dispari(10))
print(pari_dispari(17))

