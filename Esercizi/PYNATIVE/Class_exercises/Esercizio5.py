class Persona:
    def __init__(self):
        self.nome:str = ""
        self.cognome:str = "" 
        self.età:int = 0 
    
    def setName(self, nome_persona:str) -> None:
        self.nome = nome_persona 

    def setLastname(self, cognome_persona:str) -> None:
        self.cognome = cognome_persona

    def setAge(self, età_persona:str) -> None:
        self.età = età_persona

    def getName(self) -> str:
        return self.nome

    def getLastname(self) -> str:
        return self.cognome 
    
    def getAge(self) -> int:
        return self.età 
    
    def __str__(self):
        return f"Le informazioni della persona sono le seguenti:\nNome: {self.getName()}\nCognome: {self.getLastname()}\nEtà: {self.getAge()}"
    
    def __call__(self):
        if self.età < 18:
            return "La persona è minorenne."
        elif 18 <= self.età < 30:
            return "La persona è maggiorenne."
        elif 30 <= self.età <= 65:
            return "La persona è adulta."
        else:
            return "La persona è anziana."

persona1 = Persona()
persona1.setName("Lisa")
persona1.setLastname("Bandinelli")
persona1.setAge(18)
print(persona1.getName(), persona1.getLastname(), persona1.getAge())

print(persona1)
print(persona1())
    