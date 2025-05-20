import math

class DenominatoreNullo(Exception):
    pass

class FormulaError(Exception):
    pass 

class FrazioneError(Exception):
    pass

class DivisioneZero(Exception):
    pass


class Frazione:
    def __init__(self, numeratore:int, denominatore:int):
        while True: 
            try:    
                numeratore = int(input("Inserisci il numeratore della frazione: "))
                denominatore = int(input("Inserisci il denominatore della frazione: "))
                if denominatore == 0:
                    raise DenominatoreNullo("Il denominatore non può essere zero.") 
                self.numeratore = numeratore
                self.denominatore = denominatore
                self.semplifica_frazione()
            except FormulaError as e:
                print(f"Per favore inserisci numeri interi validi {e}.")

    def __str__(self):
        return f"{self.numeratore}/{self.denominatore}"
    
    def semplifica_frazione(self):
        try:
            mcd = math.gcd(self.numeratore, self.denominatore)
            self.numeratore = self.numeratore // mcd
            self.denominatore = self.denominatore // mcd    
        except FormulaError as e:
            print(e)

    def somma(self,seconda_frazione):
        try:
            if not isinstance(seconda_frazione, Frazione):
                raise FrazioneError("L'operazione richiede un oggetto Frazione.")
            numeratore = (self.numeratore * seconda_frazione.denominatore) + (self.denominatore * seconda_frazione.numeratore)
            denominatore = self.denominatore * seconda_frazione.denominatore
            return Frazione(numeratore, denominatore)
        except Exception as e:
            raise FrazioneError(f"Errore nella somma delle frazioni: {e}.")         
    
    def sottrazione(self,seconda_frazione):
        try:
            if not isinstance(seconda_frazione, Frazione):
                raise FrazioneError("L'operazione richiede un oggetto Frazione.")
            numeratore = (self.numeratore * seconda_frazione.denominatore) + (self.denominatore * seconda_frazione.numeratore)
            denominatore = self.denominatore * seconda_frazione.denominatore
            return Frazione(numeratore, denominatore)
        except Exception as e:
            raise FrazioneError(f"Errore nella sottrazione delle frazioni: {e}.")   

    def moltiplicazione(self,seconda_frazione):
        try:
            if not isinstance(seconda_frazione, Frazione):
                raise FrazioneError("L'operazione richiede un oggetto Frazione.")
            numeratore = (self.numeratore * seconda_frazione.numeratore)
            denominatore = self.denominatore * seconda_frazione.denominatore
            return Frazione(numeratore, denominatore)
        except Exception as e:
            raise FrazioneError(f"Errore nella moltiplicazione delle frazioni: {e}.") 

    def moltiplicazione(self,seconda_frazione):
        try:
            if not isinstance(seconda_frazione, Frazione):
                raise FrazioneError("L'operazione richiede un oggetto Frazione.")
            if seconda_frazione.numeratore == 0:
                raise DivisioneZero("Divisione per zero non supportata.")
            numeratore = (self.numeratore * seconda_frazione.numeratore)
            denominatore = self.denominatore * seconda_frazione.denominatore
            return Frazione(numeratore, denominatore)
        except Exception as e:
            raise FrazioneError(f"Errore nella divisione delle frazioni: {e}.")  
    
    def equivalenza(self, seconda_frazione):
        try:
            if not isinstance(seconda_frazione, Frazione):
                raise FrazioneError("L'operazione richiede un oggetto Frazione.")
            return self.numeratore*seconda_frazione.denominatore == self.denominatore*seconda_frazione.numeratore
        except Exception as e:
            raise FrazioneError(f"Errore nel controllo di equivalenza delle frazioni.")
    
    