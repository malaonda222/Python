class Rettangolo:
    def __init__(self, base: int, altezza: int) -> None:
        self.base = base 
        self.altezza = altezza 

    @property 
    def area(self):
        area = self.base * self.altezza 
        return area 

rettangolo = Rettangolo(10, 11)
print(f"Area rettangolo: {rettangolo.area}")




class Persona: 
    def __init__(self, nome: str) -> None:
        self.__nome = nome 
    
    @property
    def nome(self) -> str:
        return self.__nome 

    @nome.setter 
    def nome(self, nome: str) -> None:
        if not isinstance(nome, str):
            raise ValueError("Nome deve essere una stringa")
        else:
            self.__nome = nome 
    
persona = Persona("Mario")
persona.nome = "Adriano"
print(f"Nome: {persona.nome}")

    
