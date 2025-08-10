'''Logica: Implementa una classe Banca con metodi per deposito, prelievo e saldo.'''

class Banca:
    def __init__(self, conto: float) -> None:
        self.conto = conto 
    
    def deposito(self, somma: float) -> None:
        self.conto += somma
        print(f"Somma {somma} versata su conto")
    
    def prelievo(self, ammontare: float) -> None:
        if ammontare <= self.conto:
            print(f"Somma {ammontare} disponibile per il prelievo")
            self.conto -= ammontare
        else:
            print(f"Non ci sono abbastanza liquidità")
    
    def saldo(self) -> float:
        return f"Saldo: {self.conto}" 
    
conto1: Banca = Banca(300)
conto1.deposito(200.90)
conto1.deposito(2344.08)
conto1.prelievo(900)
conto1.prelievo(300)
print(conto1.saldo())
        
