class DenominatoreNullo(Exception):
    pass

class DivisioneperZero(Exception):
    pass

class Frazione:
    def __init__(self, numeratore:int, denominatore:int):
        self.numeratore = numeratore
        self.denominatore = denominatore 
    try:
        if denominatore == 0:
            raise DenominatoreNullo("Il denominatore non può essere zero.")
            self.semplifica()
        
    except DenominatoreNullo as e:
        print(f"Errore: {e}.")

    def __str__(self):
        return f"{self.numeratore}/{self.denominatore}"
    
    def semplifica_frazione(self):
        try:
            

