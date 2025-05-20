#Inizializzare un oggetto della classe persona

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
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("Errore! Il nome deve essere una stringa e non può essere una stringa vuota.")
        else:
            self.name = name 
    
    def setLastname(self, lastname:str) -> None:
        if not isinstance(lastname, str) or lastname.strip() == "":
            raise ValueError("Errore! Il cognome deve essere una stringa e non può essere una stringa vuota.")
        else:
            self.lastname = lastname

    def setAge(self, age:int) -> None:
        if not isinstance(age, int) and age < 0 or age > 130:
            raise ValueError("Errore! L'età deve essere un valore intero e necessariamente compreso tra 0 e 130.")
        else:
            self.age = age

    def getName(self) -> str:
        return self.name
    
    def getLastname(self) -> str:
        return self.lastname
    
    def getAge(self) -> int:
        return self.age
    
    def speak(self) -> None:
        print(f"\"Hello! My name is {self.getName()}\"\n")

    
    


