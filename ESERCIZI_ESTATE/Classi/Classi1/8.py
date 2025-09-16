'''
Esercizio 8 - Triangolo rettangolo
Tema: Python OOP - @property
Obiettivo: Proprietà calcolate dinamicamente con più attributi collegati.
Traccia:
1. Crea una classe TriangoloRettangolo con attributi _base e _altezza. 
2. Esporre base e altezza tramite @property e setter (>0).
3. Aggiungi proprietà calcolate: 
    * ipotenusa (teorema di Pitagora)
    * area = 0.5 * base * altezza
4. Implementa __str__ per stampare base, altezza, ipotenusa e area.
Suggerimento:
* Usa math.sqrt() per calcolare l’ipotenusa.
'''

class TriangoloRettangolo:
    def __init__(self, base: float, altezza: float) -> None:
        self.base = base 
        self.altezza = altezza 

    @property 
    def base(self) -> float:
        return self._base 
    
    @base.setter 
    def base(self, base: float) -> float:
        if not isinstance(base, (int, float)) or not base > 0:
            raise ValueError("Errore. La base deve essere un numero maggiore di 0")
        self._base = base 
    
    @property 
    def altezza(self) -> float:
        return self._altezza 
    
    @altezza.setter 
    def altezza(self, altezza: float) -> float:
        if not isinstance(altezza, (int, float)) or not altezza > 0:
            raise ValueError("Errore. L'altezza deve essere un numero maggiore di 0")
        self._altezza = altezza 

    @property
    def area(self) -> float:
        area = 0.5 * self._base * self._altezza 
        return area 
    
    def __str__(self):
        return f"Base: {self.base}\nAltezza: {self.altezza}\nArea: {self.area}"

triangolo = TriangoloRettangolo(10, 3)
triangolo.base = 11
triangolo.altezza = 3
print(triangolo)



    
        
