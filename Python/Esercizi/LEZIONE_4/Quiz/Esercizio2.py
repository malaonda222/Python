'''Esercizio 2'''
#funzione che ritorni un dizionario che mappa ogni elemento alla sua frequenza nella lista
def frequency_dict(elements:list) -> dict:
    dizionario_frequenze = {}
    for item in elements:
        if item in dizionario_frequenze:
            dizionario_frequenze[item] += 1 
        else:
            dizionario_frequenze[item] = 1
    
    return dizionario_frequenze





class Person:
    def __init__(self, name, age):
        self.name = name    
        self.age = age
    def __str__(self):
        return f"{self.name}, {self.age} years old"

p = Person("Luca", 30)
print(p) # Output: Luca, 30 years old



class Greeter:
    def __init__(self, message):
        self.msg = message
    def __call__(self):
        return f"Hello, {self.msg}!"
g = Greeter("Alice")
print(g()) # Output: Hello, Alice!