class Film:
    def __init__(self, titolo: str, regista: str, durata: int):
        self.titolo = titolo 
        self.regista = regista 
        self.durata = durata 

    def descrizione(self):
        print(f"\"{self.titolo}\", diretto da {self.regista}, dura {self.durata} minuti.")

    def lunghezza(self): 
        return self.durata > 120
    

film = Film("One Day", "Lone Scherfig", 125)
film.descrizione()
print(film.lunghezza())