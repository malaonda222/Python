class Animal:
    def __init__(self, name:str, legs:str):
        self.name = name
        self.legs = legs 
        print(f"Il nome dell'animale è {self.name} e ha {self.legs} gambe.")
    
    def setLegs(self, legs):
        self.legs = legs
    
    def getLegs(self):
        return self.legs
    
    def printInfo(self):
        print(f"Nome: {self.name}, Gambe: {self.legs}")


animale1 = Animal("cane", 4)
animale2 = Animal("ragno", 8)

print(f"L'animale 1 si chiama {animale1.name}.")
print(f"L'animale 2 ha {animale2.legs} gambe.")

animale1.legs = 5 #opzione 1
print(f"Nuovo numero di gambe per animale 1: {animale1.getLegs()}.")

animale2.setLegs(9) #opzione 2
print(f"Nuovo numero di gambe per animale 2: {animale2.getLegs()}.")

print(f"Numero di gambe per animale 1: {animale1.getLegs()}.")
print(f"Numero di gambe per animale 2: {animale2.getLegs()}.")

animale1.printInfo()
animale2.printInfo()



