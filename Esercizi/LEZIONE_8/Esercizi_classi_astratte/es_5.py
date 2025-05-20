from abc import ABC, abstractmethod

class Dipendente(ABC):
    def info(self):
        print("Sono un dipendente.")

    @abstractmethod
    def calcola_stipendio(self) -> None:
        pass 

class Impiegato(Dipendente):
    def calcola_stipendio(self):
        return f"Stipendio fisso 1500 euro."

class Consulente(Dipendente):
    def __init__(self, giorni_lavorati: int):
        self.giorni_lavorati = giorni_lavorati
    
    def calcola_stipendio(self):
        return f"Stipendio pari a {100*self.giorni_lavorati} euro."


dip = [Impiegato(), Consulente(10), Consulente(11)]
for item in dip:
    item.info()
    print(item.calcola_stipendio())
    print()

i: Impiegato = Impiegato()
c: Consulente = Consulente(5)
i.info()
print(i.calcola_stipendio())
print()
c.info()
print(c.calcola_stipendio())
