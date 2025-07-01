from abc import ABC, abstractmethod

class MezzoDiTrasporto(ABC):
    @abstractmethod
    def muoviti(self) -> None:
        pass 

class Bicicletta(MezzoDiTrasporto):
    def muoviti(self):
        print(f"Sto pedalando!")

class Automobile(MezzoDiTrasporto):
    def muoviti(self):
        print(f"Sto guidando un'auto!")
    
b: Bicicletta = Bicicletta()
a: Automobile = Automobile()
mezzi = [b, a]
for item in mezzi:
    item.muoviti()

