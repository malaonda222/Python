class Rectangle:
    def __init__(self, width:float, height:float):
        self.width = width
        self.height = height 
    
    def area(self):
        return self.width * self.height 
    
    def perimeter(self):
        return 2 * (self.width + self.height) 
    

rettangolo1 = Rectangle(30.5, 4)

print(f"L'area del rettangolo è {Rectangle.area(rettangolo1)} e il perimetro del rettangolo è {Rectangle.perimeter(rettangolo1)}")
print(f"L'area del rettangolo è: {rettangolo1.area()}")
print(f"Il perimetro del rettangolo è: {rettangolo1.perimeter()}")