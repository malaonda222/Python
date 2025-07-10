import random

class Creatura:
    def __init__(self, nome: str) -> None:
        self._nome = ""
        self.setNome(nome)
        
    def setNome(self, nome: str) -> None:
        if not isinstance(nome, str) or not nome.strip():
            self._nome = "Creatura Generica"

    def getNome(self) -> str:
        return self._nome 
    
    def __str__(self) -> str:
        return f"Creatura: {self._nome}"
    

class Alieno(Creatura):
    def __init__(self, nome: str):
        super().__init__(nome)
        self._matricola = self.__setMatricola()
        self._munizioni = self.__setMunizioni()
        
        nome_robot = f"Robot- {self._matricola}"
        self.setNome(nome_robot)
        if self.getNome() != nome_robot:
            print("Attenzione! Tutti gli Alieni devono avere il nome 'Robot' seguito dal numero di matricola!")
            print("Reimpostazione nome Alieno in Corso!")
            self.setNome(nome_robot)

    def __setMatricola(self) -> int:
        self._matricola = random.randint(10000, 90000)
        return self._matricola
    
    def __setMunizioni(self) -> list[int]:
        self._munizioni = [i**2 for i in range(15)]
        return self._munizioni

    def getMatricola(self) -> int:
        return self._matricola 
    
    def getMunizioni(self) -> list[int]:
        return self._munizioni 

    def __str__(self) -> str:
        return f"Alieno: {self.getNome()}"
    

class Mostro(Creatura):
    def __init__(self, nome: str, urlo_vittoria: str, gemito_sconfitta: str):
        super().__init__(nome)
        self.__setVittoria(urlo_vittoria)
        self.__setSconfitta(gemito_sconfitta)
        self.__setAssalto()
    
    def __setVittoria(self, vittoria: str):
        if isinstance(vittoria, str) and vittoria.strip() != "":
            self.__urlo_vittoria = vittoria 
        else:
            self.__urlo_vittoria = "GRAAAHHH"
    
    def __setSconfitta(self, sconfitta: str):
        if isinstance(sconfitta, str) and sconfitta.strip() != "":
            self.__gemito_sconfitta = sconfitta 
        else:
            self.__gemito_sconfitta = "Uuurghhh"

    def __setAssalto(self):
        self.__assalto = random.sample(range(1, 101), 15)
    
    def getUrloVittoria(self) -> str:
        return self.__urlo_vittoria
    
    def getGemitoSconfitta(self) -> str:
        return self.__gemito_sconfitta

    def getAssalto(self):
        return self.__assalto

    def __str__(self) -> str:
        name = ""
        indice = 0
        for element in self.getNome():
            if element.isalpha():
                if indice % 2 == 0:
                    name += element.lower()
                else:
                    name += element.upper()
                indice += 1
            else:
                name += element
                indice += 1
        return (f"Mostro: {name}")



def pariUguali(a: list[int], b: list[int]) -> list[int]:
    c: list[int] = []
    for i in range(len(a)):
        if a[i] % 2 == 0 and b[i] % 2 == 0:
            c.append(1)
        else:
            c.append(0)
    return c


def combattimento(a: Alieno, m: Mostro):
    if not isinstance(a, Alieno) or not isinstance(m, Mostro):
        print(f"Combattimento interrotto.")
        return None 
    else:
        result = pariUguali(a.getMunizioni(), m.getAssalto())
        conteggio = result.count(1)
        if conteggio > 4:
            print("Mostro vince!")
            print(m.getUrloVittoria())
            print(m.getUrloVittoria())
            print(m.getUrloVittoria())
            return m
        else:
            print("Alieno vince!")
            print(m.getGemitoSconfitta())
            return a


def proclamaVincitore(c: Creatura):
    if not isinstance(c, Creatura):
        print("Oggetto non valido. Deve essere una creatura.")
        return 
    
    testo: str = c.__str__()
    lunghezza = len(testo)+10
    altezza = 5

    for i in range(5):
        if i == 0 or i == altezza-1:
            print("*"*lunghezza)
        elif i == 2:
            print("*" + " " * 4 + testo + " " * 4 + "*")
        else:
            print("*" + ((lunghezza-2)* " ") + "*")
    return c



if __name__ == '__main__':
    mostro = Mostro("Godzilla", "GRAAAHHH", "Uuurghhh")
    alieno = Alieno("Yoki")

    print(mostro)
    print(mostro.getAssalto())
    print()
    print(alieno)
    print(alieno.getMunizioni())
    print()

    print("---COMBATTIMENTO---")
    combattimento(alieno, mostro)
    print()

    vincitore = mostro if pariUguali(alieno.getMunizioni(), mostro.getAssalto()).count(1) > 4 else alieno 
    print("---VINCITORE---")
    proclamaVincitore(vincitore)