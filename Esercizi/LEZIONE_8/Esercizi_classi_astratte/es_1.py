from abc import ABC, abstractmethod

class Figura(ABC):

    @abstractmethod
    def calcola_area(self) -> None:
        pass 

class Rettangolo(Figura):
    def __init__(self, base: float, altezza: float):
        self.base = base 
        self.altezza = altezza 

    def calcola_area(self):
        return f"Area del rettangolo: {self.base * self.altezza}."
    
class Quadrato(Figura):
    def __init__(self, lato: float):
        self.lato = lato 
    
    def calcola_area(self):
        return f"Area del quadrato: {self.lato * self.lato}." 

rettangolo: Rettangolo = Rettangolo(4, 5)
print(rettangolo.calcola_area())
quadrato: Quadrato = Quadrato(3)
print(quadrato.calcola_area())