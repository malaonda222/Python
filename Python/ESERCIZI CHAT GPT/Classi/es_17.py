'''
Classe Quadrato
Classe Quadrato con:
Attributo: lato
Metodi:
area() → restituisce l’area del quadrato
perimetro() → restituisce il perimetro
'''

class Quadrato:
    def __init__(self, lato:float):
        self.lato = lato 

    def area(self):
        return self.lato*self.lato
    
    def perimetro(self):
        return self.lato * 4
    
    def __str__(self):
        return f"Il lato del quadrato è {self.lato} cm\nL'area del quadrato è {self.area()} cm\nIl perimetro del quadrato è {self.perimetro()} cm"
    
quadrato = Quadrato(5)
print(quadrato.area())
print(quadrato.perimetro())
print(quadrato)