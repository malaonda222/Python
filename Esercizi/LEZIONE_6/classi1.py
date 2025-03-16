class Persona:
    def __init__(self, nome, cognome): #costruttore che viene chiamato automaticamente
        self.nome = nome        #sono delle caratteristiche
        self.cognome = cognome
    
    def saluta(self):
        print(f"Ciao sono {self.nome} {self.cognome}")

person1 = Persona("Luca", "Rossi")
person2 = Persona("Marco", "Verdi")

print(person1.cognome)
print(person2.nome)

person1.saluta()

person2.nome = "Maria"

person2.saluta ()