'''Esercizio 7 - Cerchio
Tema: Python OOP - @property
Obiettivo: Proprietà calcolate dinamicamente da un singolo attributo.
Traccia:
1. Crea una classe Cerchio con attributo _raggio.
2. Esporre il raggio tramite @property e setter (raggio >0).
3. Aggiungi proprietà calcolate:
    * area = π * raggio²
    * circonferenza = 2 * π * raggio
4. Implementa __str__ per stampare raggio, area e circonferenza.
5. Crea un oggetto cerchio e prova a modificare il raggio tramite setter.
Suggerimento:
* Usa il modulo math per π.
'''
import math
class Cerchio:
    def __init__(self, raggio: float) -> None:
        self.raggio = raggio

    @property
    def raggio(self) -> float:
        return self._raggio 
    
    @raggio.setter
    def raggio(self, raggio: float) -> None:
        if not isinstance(raggio, (int,float)) or raggio <= 0:
            raise ValueError("Errore. Il raggio non può essere inferiore a 0")
        self._raggio = raggio 
    
    @property
    def area(self) -> float:
        area = f"{math.pi * self._raggio**2:.2f}"
        return area
    
    @property
    def circonferenza(self) -> float:
        circonferenza = f"{2 * math.pi * self._raggio:.2f}"
        return circonferenza 
    
    def __str__(self) -> str:
        return f"Raggio: {self.raggio}\nArea: {self.area}\nCirconferenza: {self.circonferenza}"
    
cerchio = Cerchio(3)
cerchio.raggio = 10
print(f"Area: {cerchio.area}")
print(f"Circonferenza: {cerchio.circonferenza}")
