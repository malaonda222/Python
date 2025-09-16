'''Esercizio 3 - Rettangolo con più proprietà collegate
Traccia:
1. Crea una classe Rettangolo con attributi protetti _larghezza e _altezza.
2. Esporre larghezza e altezza tramite @property e setter con validazione (devono essere >0).
3. Aggiungi proprietà calcolate area e perimetro (solo getter).
4. Dimostra l’uso creando un rettangolo, stampando area e perimetro, e aggiornando larghezza o altezza.
'''

class Rettangolo:
    def __init__(self, larghezza: int, altezza: int) -> None:
        self.larghezza = larghezza 
        self.altezza = altezza

    @property 
    def larghezza(self) -> int:
        return self._larghezza 
    
    @larghezza.setter
    def larghezza(self, larghezza: int) -> None:
        if self.larghezza <= 0 :
            raise ValueError("La larghezza non può essere inferiore a 0")
        self._larghezza = larghezza
    
    @property
    def altezza(self) -> int:
        return self._altezza 
    
    @altezza.setter 
    def altezza(self, altezza: int) -> None:
        if self.altezza <= 0:
            raise ValueError("L'altezza non può essere inferiore a 0")
        self._altezza = altezza 
    
    @property 
    def area(self):
        return self._altezza * self._larghezza 
    
    @property
    def perimetro(self):
        return (self._altezza + self._larghezza)*2
    
rettangolo = Rettangolo(10, 5)
print("Area: ", rettangolo.area)
print("Perimetro: ", rettangolo.perimetro)

rettangolo.altezza = 6 
print("Area: ", rettangolo.area)
print("Perimetro: ", rettangolo.perimento)
