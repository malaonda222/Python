'''
Esercizio 5 - Controllo velocità auto
Tema: Python OOP - @property
Obiettivo: Rinforzare l’uso di @property e setter con validazione per valori numerici.
Traccia:
1. Crea una classe Auto con un attributo _velocita (float) che rappresenta la velocità in km/h.
2. Esporre l’attributo tramite @property e setter, assicurandoti che:
    * Il valore sia un numero (int o float).
    * La velocità sia compresa tra 0 e 300 km/h.
3. Implementa __str__ per stampare la velocità attuale dell’auto.
4. Crea un oggetto Auto e prova a modificare la velocità tramite il setter, testando valori validi e non validi.
Suggerimento:
* Usa la logica di validazione direttamente nel setter.
* Assegna il valore iniziale nell’__init__ passando dal setter per applicare subito la validazione.
'''

class Auto:
    def __init__(self, velocita: float) -> None:
        self.velocita = velocita 

    @property 
    def velocita(self) -> float:
        return self._velocita 
    
    @velocita.setter 
    def velocita(self, velocita: float) -> None:
        if not isinstance(velocita, (int|float)) or not 0 < velocita < 300:
            raise ValueError("Velocità non amessa")
        self._velocita = velocita
    
    def __str__(self) -> str:
        return f"Velocità auto: {self.velocita} km/h"
    
mercedes = Auto(100)
print(f"Velocità:",mercedes.velocita)

mercedes.velocita = 30
print("Velocità:", mercedes.velocita)
print(mercedes)

