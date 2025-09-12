class Persona:
    def __init__(self, eta: int) -> None:
        self._eta = eta 
    
    @property
    def eta(self) -> str:
        return self._eta 
    
    @eta.setter
    def eta(self, eta: int) -> None:
        if not isinstance(eta, int) or eta < 0:
            raise ValueError("L'età non può essere negativa")
        self._eta = eta 

Cecilia = Persona(18)
print(f"Età di Cecilia: {Cecilia.eta}")
    