'''Crea una classe Persona con attributi nome, eta'''

class Persona:
    def __init__(self, nome: str, eta: int) -> None:
        self.set_nome(nome)
        self.set_eta(eta)
    
    def set_nome(self, nome: str) -> str:
        if not isinstance(nome, str):
            raise ValueError("Il nome deve essere una stringa")
        self.nome = nome 
    
    def set_eta(self, eta: int) -> int:
        if not isinstance(eta, int):
            raise ValueError("L'età deve essere un numero")
        self.eta = eta 
    
    def get_nome(self) -> str:
        return self.nome 
    
    def get_eta(self) -> int:
        return self.eta 
    
    def saluta(self) -> None:
        return f"Ciao {self.get_nome()}!"
    
    def maggiorenne(self) -> bool:
        if self.get_eta() >= 18:
            return f"{self.get_nome()} è maggiorenne"
        else:
            return f"{self.get_nome()} è minorenne"

    def __str__(self):
        return f"Nome: {self.get_nome()}\nEtà: {self.get_eta()}"
    
class Studente(Persona):
    def __init__(self, nome: str, eta: int, corso: str, matricola: int) -> None:
        super().__init__(nome, eta)
        self.set_corso(corso)
        self.set_matricola(matricola)

    def set_corso(self, corso: str) -> None:
        if not isinstance(corso, str):
            print("Il corso deve essere una stringa")
        self.corso = corso 

    def set_matricola(self, matricola: int) -> None:
        if not isinstance(matricola, int):
            print("Il numero di matricola deve essere un intero")
        self.matricola = matricola 
    
    def get_nome(self) -> str:
        return self.nome 
    
    def get_eta(self) -> int:
        return self.eta 
    
    def get_corso(self) -> str:
        return self.corso 
    
    def get_matricola(self) -> int:
        return self.matricola
    
    def saluta(self) -> str:
        return f"Ciao studente {self.get_nome()}"
    
    def __str__(self) -> str:
        return f"Nome: {self.get_nome()}\nEtà: {self.get_eta()}\nCorso: {self.corso()}\nMatricola: {self.get_matricola()}"
    
 
persona1: Persona = Persona(nome="Lisa", eta=44)
print(persona1)
print(persona1.saluta())
print(persona1.maggiorenne())
print()
persona2: Persona = Persona("Simone", 60)
print(persona2)
print(persona2.saluta())
print(persona2.maggiorenne())