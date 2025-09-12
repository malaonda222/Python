'''
Esercizio 6 - Rettangolo avanzato
Tema: Python OOP - @property
Obiettivo: Gestire proprietà calcolate dinamicamente.
Traccia:
1. Crea una classe Rettangolo con attributi _larghezza e _altezza.
2. Esporre larghezza e altezza tramite @property e setter con validazione (>0).
3. Aggiungi proprietà calcolate area e perimetro (solo getter).
4. Implementa __str__ per stampare larghezza, altezza, area e perimetro.
5. Crea un oggetto rettangolo e prova a modificare larghezza o altezza tramite setter.
Suggerimento:
* Usa i setter anche nell’__init__ per applicare la validazione fin dall’inizio.
'''


class Rettangolo:
    def __init__(self, larghezza: float, altezza: float) -> None:
        self.larghezza = larghezza 
        self.altezza = altezza 

    @property
    def larghezza(self) -> float:
        return self._larghezza
    
    @larghezza.setter
    def larghezza(self, larghezza: float) -> None:
        if not isinstance(larghezza, (int, float)) or larghezza <= 0:
            raise ValueError("Errore. La larghezza non può essere inferiore a 0")
        self._larghezza = larghezza 
    
    @property
    def altezza(self) -> int:
        return self._altezza 
    
    @altezza.setter 
    def altezza(self, altezza: int) -> None:
        if not isinstance(altezza, (int, float)) or altezza <= 0:
            raise ValueError("L'altezza non può essere inferiore a 0")
        self._altezza = altezza

    @property
    def area(self) -> float:
        return self._altezza*self._larghezza 
    
    @property 
    def perimetro(self) -> float:
        return (self._altezza + self._larghezza)* 2

    def __str__(self) -> str:
        return f"Larghezza: {self.larghezza}\nAltezza: {self.altezza}\nArea: {self.area}\nPerimetro: {self.perimetro}"


rettangolo = Rettangolo(10, 5)
print("Area:",rettangolo.area)
print("Perimetro:",rettangolo.perimetro)

rettangolo.altezza = 6 
print("Area:",rettangolo.area)
print("Perimetro:",rettangolo.perimetro)

print(rettangolo)