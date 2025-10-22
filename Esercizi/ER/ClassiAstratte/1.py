'''Esercizio 1 – Base
Obiettivo: Capire la struttura e l’uso minimo di una classe astratta.
Nome dell’esercizio: FormaGeometrica
Traccia:
1. Crea una classe astratta chiamata FormaGeometrica con:
2. Un metodo astratto area()
3. Un metodo astratto perimetro()
4. Crea due classi concrete che la estendono: Rettangolo e Cerchio.
Implementa i due metodi per ciascuna forma.
Crea e stampa area e perimetro di entrambe.
Suggerimento: usa from abc import ABC, abstractmethod'''

from abc import ABC, abstractmethod
import math

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self) -> float:
        pass 

    @abstractmethod
    def perimetro(self) -> float:
        pass 

class Rettangolo(FormaGeometrica):
    def __init__(self, base: float, altezza: float) -> None:
        self.base = base 
        self.altezza = altezza 

    def area(self) -> float:
        return f"Area rettangolo: {self.base*self.altezza:.2f}"
    
    def perimetro(self) -> float:
        return f"Perimetro rettangolo: {(self.base + self.altezza)*2:.2f}"

class Cerchio(FormaGeometrica):
    def __init__(self, raggio: float) -> None:
        self.raggio = raggio 

    def area(self) -> float:
        return f"Area cerchio: {math.pi * (self.raggio**2):.2f}"
    
    def perimetro(self) -> float:
        return f"Perimetro cerchio: {2*math.pi*self.raggio:.2f}"
    

rettangolo = Rettangolo(4.5, 6.7)
cerchio = Cerchio(5.7)

print(rettangolo.area())
print(rettangolo.perimetro())

print(cerchio.area())
print(cerchio.perimetro())
