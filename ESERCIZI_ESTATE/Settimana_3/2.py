'''Logica: Crea una classe Contatore che tiene traccia delle chiamate.'''

class Contatore:
    def __init__(self):
        self.contatore = 0

    def incrementa(self):
        self.contatore += 1 

    def decrementa(self):
        self.contatore -= 1

    def leggi_contatore(self):
        return self.contatore 

    def resetta_contatore(self):
        self.contatore = 0
    

cont: Contatore = Contatore()
cont.incrementa()
cont.incrementa()
cont.incrementa()
cont.decrementa()
print(cont.leggi_contatore())

cont.resetta_contatore()
print(cont.leggi_contatore())


class Contatore:
    def __init__(self):
        self.contatore = 0

    def incrementa(self) -> None:
        self.contatore += 1

    def decrementa(self) -> None:
        self.contatore -= 1
    
    def visualizza(self) -> None:
        return self.contatore
    
    def resetta(self) -> None:
        self.contatore = 0 

