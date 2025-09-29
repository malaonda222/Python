from abc import ABC, abstractmethod

class Forma(ABC):
    def __init__(self, nome_forma: str) -> None:
        self.nome_forma = nome_forma
    
    @abstractmethod
    def getArea(self) -> None:
        pass 

    @abstractmethod
    def render(self) -> None:
        pass 


class Quadrato(Forma):
    def __init__(self, lato: int, nome_forma: str = "Quadrato") -> None:
        super().__init__(nome_forma)
        self.lato = lato 

    def getArea(self) -> float:
        return self.lato ** 2

    def render(self):
        print(f"Ecco un {self.nome_forma} di lato {self.lato}!")
        for i in range(self.lato):
            for j in range(self.lato):
                if i == 0 or i == self.lato-1 or j == 0 or j == self.lato-1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        print(f"L'area di questo quadrato vale: {self.getArea()}")
   

class Rettangolo(Forma):
    def __init__(self, base: int, altezza: int) -> None:
        super().__init__("Rettangolo")
        self.base = base 
        self.altezza = altezza 
    
    def getArea(self) -> int:
        return self.base * self.altezza 
    
    def render(self):
        print(f"Ecco un {self.nome_forma} di base {self.base} e altezza {self.altezza}")
        for i in range(self.altezza):
            for j in range(self.base):
                if i == 0 or i == self.altezza-1 or j == 0 or j == self.base-1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        print(f"L'area di questo rettangolo vale: {self.getArea()}")
    

class Triangolo(Forma):
    def __init__(self, lato: int) -> None:
        super().__init__("Triangolo")
        self.lato = lato

    def getArea(self) -> float:
        return self.lato * self.lato / 2

    def render(self):
        print(f"Ecco un {self.nome_forma} di lato {self.lato}")
        for i in range(1, self.lato+1):
            for j in range(1, i + 1):
                if i == self.lato or j == i or j == 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        print(f"L'area di questo triangolo vale: {self.getArea()}")


    def render2(self):
        print(f"Ecco un {self.nome_forma} di lato {self.lato}")
        for i in range(1, self.lato + 1):
            for j in range(1, self.lato + 1):
                if i == self.lato or j == self.lato or j == self.lato - i + 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        print(f"L'area di questo triangolo vale: {self.getArea()}")

quadrato = Quadrato(4)
quadrato.render()

rettangolo = Rettangolo(8, 3)
rettangolo.render()

triangolo = Triangolo(5)
triangolo.render()
triangolo.render2()