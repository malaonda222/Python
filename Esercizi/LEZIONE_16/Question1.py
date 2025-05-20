class Contatore:
    def __init__(self, conteggio: int = 0):
        self.conteggio = conteggio

    def setZero(self) -> None: 
        self.conteggio = 0

    def add1(self):
        self.conteggio += 1

    def sub1(self):
        if self.conteggio <= 0:
            print("Non è possibile eseguire la sottrazione")
        else: 
            self.conteggio -= 1

    def get(self) -> int:
        return self.conteggio 
    
    def mostra(self) -> None:
        print(f"Conteggio attuale: {self.conteggio}")


c = Contatore()  
c.add1() 
c.mostra()
    
