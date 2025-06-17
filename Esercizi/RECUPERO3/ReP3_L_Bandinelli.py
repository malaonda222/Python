from random import randint

class Creatura:
    def __init__(self, nome: str) -> None:
        self._nome = ""
        self.setNome(nome)
        
    def setNome(self, nome: str) -> None:
        if not isinstance(nome, str) or not nome.strip():
            self._nome = "Creatura Generica"
        self._nome = nome

    def getNome(self) -> str:
        return self._nome 
    
    def __str__(self) -> str:
        return f"Creatura: {self._nome}"
    

class Alieno(Creatura):
    def __init__(self, nome: str):
        super().__init__(nome)
        self._matricola = self._setMatricola()
        self._munizioni = self._setMunizioni()
        
        nome_robot = f"Robot- {self._matricola}"
        self.setNome(nome_robot)
        if self.getNome() != nome_robot:
            print("Attenzione! Tutti gli Alieni devono avere il nome 'Robot' seguito dal numero di matricola!")
            print("Reimpostazione nome Alieno in Corso!")
            self.setNome(nome_robot)

    def _setMatricola(self) -> int:
        self._matricola = randint(10000, 90000)
        return self._matricola
    
    def _setMunizioni(self) -> list[int]:
        self._munizioni = [i**2 for i in range(15)]
        return self._munizioni

    def _getMatricola(self) -> int:
        return self._matricola 
    
    def _getMunizioni(self) -> list[int]:
        return self._munizioni 

    def _str__(self) -> str:
        return f"Alieno: {self.getNome}"
    
    
