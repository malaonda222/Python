class Timer:
    def __init__(self):
        self.secondi = 0
    
    def aggiungi_secondi(self, x: int):
        if x > 0:
            self.secondi += x
        else:
            print("Puoi aggiungere solo un numero positivo di secondi.")
    
    def azzera(self):
        self.secondi = 0
        print(f"Timer riazzerato.")

    def mostra_tempo(self):
        minuti = self.secondi // 60
        secondi = self.secondi % 60
        print(f"{minuti:02}:{secondi:02}")

timer = Timer()
timer.aggiungi_secondi(45)
timer.mostra_tempo()
timer.aggiungi_secondi(60)
timer.mostra_tempo()
timer.aggiungi_secondi(55)
timer.mostra_tempo()
timer.azzera()