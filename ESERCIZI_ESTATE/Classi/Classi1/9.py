'''Esercizio 9 - Cubo
Tema: Python OOP - @property
Obiettivo: Proprietà calcolate dinamicamente (3D).
Traccia: 
1. Crea una classe Cubo con attributo _lato.
2. Esporre lato tramite @property e setter (>0).
3. Aggiungi proprietà calcolate:
    * volume = lato³
    * superficie = 6 * lato²
4. Implementa __str__ per stampare lato, volume e superficie.
Suggerimento:
* Setter utilizzato anche nell’__init__.
'''

class Cubo:
    def __init__(self, lato: float|int) -> None:
        self.lato = lato 

    @property
    def lato(self) -> int|float:
        return self._lato 
    
    @lato.setter 
    def lato(self, lato: int|float) -> None:
        if not isinstance(lato, (int, float)) or not lato > 0:
            raise ValueError("Errore")
        self._lato = lato 

    @property
    def volume(self) -> float:
        return self._lato ** 3
    
    @property
    def superficie(self) -> int|float:
        superficie = 6 * self._lato ** 2
        return superficie
    
    def __str__(self) -> str:
        return f"Lato: {self.lato}\nSuperficie: {self.superficie}"

cubo = Cubo(4)
cubo.lato = 3
print(cubo.superficie)
print(cubo.volume)
print(cubo)
