'''Esercizio 10 - Controllo rettangolo modificabile
Tema: Python OOP - @property
Obiettivo: Proprietà calcolate con aggiornamento dinamico e validazioni multiple.
Traccia:
1. Crea una classe RettangoloModificabile con _larghezza e _altezza.
2. Esporre larghezza e altezza tramite @property e setter con validazione (>0).
3. Aggiungi proprietà calcolate:
    * area
    * perimetro
    * diagonale (teorema di Pitagora)
4. Implementa __str__ per stampare larghezza, altezza, area, perimetro e diagonale.
5. Crea un oggetto rettangolo modificabile e prova a cambiare larghezza/altezza tramite setter, 
    verificando aggiornamenti automatici di tutte le proprietà.
Suggerimento:
* Usa math.sqrt() per la diagonale.
'''

import math 

class RettangoloModificabile:
    def __init__(self, larghezza: float|int, altezza: float|int) -> None:
        self.larghezza = larghezza 
        self.altezza = altezza 

    @property 
    def larghezza(self) -> float|int:
        return self._larghezza 
    
    @larghezza.setter 
    def larghezza(self, larghezza: float|int) -> None:
        if not isinstance(larghezza, (int, float)) or larghezza < 0:
            raise ValueError("Errore. La larghezza non può essere inferiore a zero")
        self._larghezza = larghezza 

    @property 
    def altezza(self) -> float|int:
        return self._altezza 
    
    @altezza.setter 
    def altezza(self, altezza: float|int) -> None:
        if not isinstance(altezza, (int, float)) or altezza < 0:
            raise ValueError("Errore. La larghezza non può essere inferiore a zero")
        self._altezza = altezza 
    
    @property
    def area(self) -> float|int:
        return self._larghezza * self._altezza 
    
    @property
    def perimetro(self) -> float|int:
        return (self._larghezza + self._altezza) * 2
    
    @property 
    def diagonale(self) -> float|int:
        diagonale = math.sqrt(self._larghezza**2 + self._altezza**2)**0.5
        return f"{diagonale:.2f}"
    
    def __str__(self) -> str:
        return f"Larghezza: {self.larghezza}\nAltezza: {self.altezza}\nArea: {self.area}\nPerimetro: {self.perimetro}\nDiagonale: {self.diagonale}"
    
rettangolo = RettangoloModificabile(10, 5)
rettangolo.larghezza = 10
rettangolo.altezza = 5
print(rettangolo)
print()
rettangolo.larghezza = 8
rettangolo.altezza = 2 
print(rettangolo)
