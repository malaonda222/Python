'''Di una persona dobbiamo sapere delle informazioni.
Queste informazioni vengono chiamate attributi (della classe Persona).
Le informazioni saranno:
- nome 
- cognome
- età

come li rappresentiamo in Python?

self.name:str (attributo di tipo stringa)
self.lastname:str (attributo di tipo stringa)
self.age:int (attributo di tipo intero)'''


class Persona: 
 
# costruttore  
    def __init__(self, name:str, lastname:str, age:int): #self serve per indicare che questa è una funzione della classe Persona e in particolare il suo costruttore
        self.name = name
        self.lastname = lastname #attributo della classe Persona name si inizializza con il valore di una stringa generica "name", "lastname", "age"
        self.age = age
    

