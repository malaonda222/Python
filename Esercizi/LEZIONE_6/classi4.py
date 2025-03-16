class Cane:
    def __init__(self, nome, età, razza):
        self.nome = nome
        self.età = età
        self.razza = razza

    def descrizione(self):
        print(f"Il nome del cane è {self.nome}, ha {self.età} anni e la sua razza è {self.razza}")
    
    def abbaia(self):
        print(f"Il cane {self.nome} abbaia!")
    
    def compleanno(self):
        self.età += 1
        print(f"Il cane quest'anno compirà {self.età} anni!")

cane_uno = Cane("Pippo", 3, "Labrador")

print(cane_uno.descrizione())

cane_uno.abbaia()

cane_uno.compleanno()
print(cane_uno.descrizione())
