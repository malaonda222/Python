# Somma di due numeri
from typing import Callable

somma: Callable[[float, float], float] = lambda a, b: a + b 
print(somma(89654, 42587)) 


def somma(a:float, b:float) -> float:
    return a + b 
