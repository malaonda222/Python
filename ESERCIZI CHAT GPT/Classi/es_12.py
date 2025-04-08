class Persona:
    def __init__ (self, nome:str, età:int, sesso:str):
        self.nome = nome
        self.età = età
        self.sesso = sesso 
    
    def descrizione(self):
        return f"{self.nome}, {self.età} anni, {self.sesso}"
    
persona1 = Persona("Gina", 34, "Femmina")
print(persona1.descrizione())