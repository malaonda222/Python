# Ordinamento con sorted()
from typing import Callable 

studenti = [("Luca", 21), ("Susanna", 19), ("Marco", 22)]

lista_ordinata_numeri:Callable[[str, int], int] = sorted(studenti, key=lambda age: age[1])
print(lista_ordinata_numeri)

lista_ordinata_lettere:list[int] = sorted(studenti, key= lambda name: name[0])
print(lista_ordinata_lettere)