# Uso con filter()
from typing import Callable 

numeri:list[int] = [5, 12, 17, 18, 24, 32]
numeri_pari:Callable[[int], int] = list(filter(lambda x: x % 2 == 0, numeri))
print(numeri_pari)


def numeri_pari(numbers:list[int]):
    numeri_pari = []
    for item in numbers:
        if item % 2 == 0:
            numeri_pari.append(item) 
    return numeri_pari 

numbers:list = [5, 12, 17, 18, 24, 32]
print(numeri_pari(numbers))



evens = [x for x in numeri if x % 2 == 0]
print(evens)