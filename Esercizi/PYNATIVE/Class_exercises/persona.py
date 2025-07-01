class Persona:
    def __init__(self, nome, cognome, età):
        self.nome:str = nome
        self.cognome:str = cognome
        self.età:int = età
    
    def setName(self, nome_persona:str) -> None:
        if nome_persona:
            self.nome = nome_persona 
        else:
            print("Errore! Il nome non può essere una stringa vuota.")

    def setLastname(self, cognome_persona:str) -> None:
        if cognome_persona:
            self.cognome = cognome_persona
        else:
            print("Errore! Il cognome non può essere una stringa vuota.")

    def setAge(self, età:int) -> None:
        if età < 0 or età > 130:
            self.età = 0
        else:
            self.età = età

    def getName(self) -> str:
        return self.nome

    def getLastname(self) -> str:
        return self.cognome 
    
    def getAge(self) -> int:
        return self.età 
    
    def __str__(self):
        return f"Le informazioni della persona sono le seguenti:\nNome: {self.getName()}\nCognome: {self.getLastname()}\nEtà: {self.getAge()}\n"
    
    def __call__(self):
        if self.età < 18:
            return "La persona è minorenne."
        elif 18 <= self.età < 30:
            return "La persona è maggiorenne."
        elif 30 <= self.età <= 65:
            return "La persona è adulta."
        else:
            return "La persona è anziana."

if __name__ == "__main__":
    persona1 = Persona()
    persona1.setName("Lisa")
    persona1.setLastname("Bandinelli")
    persona1.setAge(18)
    print(persona1.getName(), persona1.getLastname(), persona1.getAge())

    print(persona1)
    print(persona1())

