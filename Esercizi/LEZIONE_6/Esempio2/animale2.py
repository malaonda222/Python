class Animale2:
    def __init__(self):
        self.nome = ""
        self.razza = ""
        self.zampe = 0
        self.colore = ""

    def displayData(self) -> None:
        print(f"Nome: {self.nome}\nRazza: {self.razza}\nZampe: {self.zampe}\nColore: {self.colore}")

    def setName(self, nome:str) -> None:
        self.nome = nome
    
    def setRace(self, razza:str) -> None:
        self.razza = razza

    def setPaw(self, zampe:int) -> None:
        self.zampe = zampe 
    
    def setColour(self, colore:str) -> None:
        self.colore = colore
    
    def getName(self) -> str:
        return self.nome
    
    def getRace(self) -> str:
        return self.razza 
    
    def getPaw(self) -> int:
        return self.zampe 
    
    def getColour(self) -> int:
        return self.colore 
    
