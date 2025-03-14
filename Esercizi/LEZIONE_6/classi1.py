class Persona:
    def __init__(self, nome, cognome): #costruttore che viene chiamato automaticamente
        self.nome = nome        #sono delle caratteristiche
        self.cognome = cognome
    
    def saluta(self):
        print("Ciao sono " + self.nome)

person1 = Persona("Luca", "Rossi")
person2 = Persona("Marco", "Verdi")

print(person1.nome)
print(person2.nome)

person1.saluta()

person2.nome = "Maria"

person2.saluta ()