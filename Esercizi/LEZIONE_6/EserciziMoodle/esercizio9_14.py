import random 

class LotteryMachine:
    def __init__(self):
        self.elementi = [str(elemento) for elemento in range(10)] + ['A', 'B', 'C', 'D', 'E']
        
    def bigliettoVincente(self):
        self.vincente = random.sample(self.elementi, 4)
    
    def displayVincente(self):
        print(f"Numeri/Lettere vincenti sono: {', '.join(self.vincente)}.")
        print("Qualsiasi biglietto che corrisponde ai 4 elementi vince un premio.")

    def verificaTicket(self, biglietto):
        if sorted(biglietto) == sorted(self.vincente):
            return "Hai vinto!"
        else:
            return "Hai perso!"

    

lotteria = LotteryMachine()
lotteria.bigliettoVincente()
lotteria.displayVincente()

biglietto = ['A', 'B', '3', '6']
print(lotteria.verificaTicket(biglietto))


