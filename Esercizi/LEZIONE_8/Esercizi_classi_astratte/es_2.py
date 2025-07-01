from abc import ABC, abstractmethod

class Animale(ABC):
    @abstractmethod
    def verso(self) -> None:
        pass 

    def descrizione(self):
        print("Questo è un animale.")

class Cane(Animale):

    def verso(self):
        print("Bau")
    
class Gatto(Animale):
    
    def verso(self):
        print("Miao")

    
cane: Cane = Cane()
cane.descrizione()
cane.verso()
gatto: Gatto = Gatto()
gatto.descrizione()
gatto.verso()