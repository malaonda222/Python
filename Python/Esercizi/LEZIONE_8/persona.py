class Persona:
    def __init__(self, name:str, lastname:str, age:int):
        self.setName(name)
        self.setLastname(lastname) 
        self.setAge(age)

    def __str__(self):
        return f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}"
    
    def __call__(self):
        if self.age < 18:
            print(f"{self.name}{self.lastname} è minorenne!")
        if 18 <= self.age < 30:
            print(f"{self.name}{self.lastname} è maggiorenne!")
        if 30 <= self.age < 80:
            print(f"{self.name}{self.lastname} è una persona adulta!")
        else:
            print(f"{self.name}{self.lastname} è una persona anziana!")


    def setName(self, name:str) -> None:
        if name:
            self.name = name 
        else:
            print("Errore! Il nome non può essere una stringa vuota.")
    
    def setLastname(self, lastname:str) -> None:
        if lastname:
            self.lastname = lastname
        else:
            print("Errore! Il cognome non può essere una stringa vuota.")

    def setAge(self, age:int) -> None:
        if age < 0 or age > 130:
            self.age = 0
        else:
            self.age = age

    def getName(self) -> str:
        return self.name
    
    def getLastname(self) -> str:
        return self.lastname
    
    def getName(self) -> int:
        return self.age
    

lb:Persona = Persona("Marco", "Rossi", 90) 
lb()
print(lb.__str__())
