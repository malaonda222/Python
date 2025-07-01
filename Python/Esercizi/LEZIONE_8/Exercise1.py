from abc import ABC, abstractmethod 
import math

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass 

class Circle(Shape):
    def __init__(self, raggio: float):
        self.raggio = raggio 

    def area(self) -> float:
        return math.pi*(self.raggio**2)
    
    def perimeter(self):
        return (math.pi*2)*self.raggio 

class Rectangle(Shape):
    def __init__(self, base: float, altezza: float) -> float:
        self.base = base 
        self.altezza = altezza 

    def area(self):
        return self.base*self.altezza
    
    def perimeter(self):
        return self.base*2 + self.altezza*2 #oppure (self.base + self.altezza) * 2
    

cerchio: Circle = Circle(3)
print(f"Area del cerchio: {cerchio.area():.2f} cm2.")
print(f"Perimetro del cerchio: {cerchio.perimeter():.2f} cm.")

rettangolo: Rectangle = Rectangle(20, 16)
print(f"Area del rettangolo: {rettangolo.area():.2f} cm2.")
print(f"Perimetro del rettangolo: {rettangolo.perimeter():.2f} cm.")

