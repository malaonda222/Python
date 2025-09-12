'''
Esercizio 4 - Temperatura valida
Tema: Python OOP - @property
Obiettivo: Consolidare l’uso di @property e setter con validazione.
Traccia:
1. Crea una classe Temperatura con un attributo _gradi.
2. Esporre l’attributo tramite @property e setter, assicurandoti che:
    * Il valore sia un numero (int o float).
    * La temperatura sia compresa tra -273.15 e 1000.
3. Implementa __str__ per stampare la temperatura in gradi Celsius.
4. Crea un oggetto Temperatura e prova a modificare il valore tramite il setter.
Suggerimento:
* Usa la logica di validazione direttamente nel setter.
* Nell’__init__, assegna il valore passando dal setter per applicare subito la validazione.
'''

class Temperatura: 
    def __init__(self, gradi: int) -> None:
        self.gradi = gradi 
    
    @property
    def gradi(self) -> int:
        return self._gradi 
    
    @gradi.setter
    def gradi(self, gradi: int) -> None:
        if not isinstance(gradi, (int|float)) or not -275.15 < gradi < 1000:
            raise ValueError("Temperatura non valida")
        self._gradi = gradi 
    
    def __str__(self) -> str:
        return f"Temperatura: {self.gradi}°C"

temp = Temperatura(10)
print("Gradi:", temp.gradi)
temp.gradi = 18
print("Gradi:", temp.gradi)
print(temp)
    