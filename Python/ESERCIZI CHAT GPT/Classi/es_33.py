import math

class Frazione:
    def __init__(self, numeratore: int, denominatore: int):
        if denominatore == 0:
            print("Errore. Inserire un denominatore diverso da zero.")
        self.numeratore = numeratore
        self.denominatore = denominatore 

    def semplifica(self):
        mcd = math.gcd(self.numeratore, self.denominatore)
        self.numeratore // mcd 
        self.denominatore // mcd 

    def mostra(self):
        print(f"{self.numeratore}/{self.denominatore}")
    
    def valore(self):
        return self.numeratore / self.denominatore
    
frazione = Frazione(10, 20)
frazione.semplifica()
frazione.mostra()
print(frazione.valore())
