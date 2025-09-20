from __future__ import annotations
from film import Film


class Azione(Film):
    def __init__(self, id_film: int, title: str, genere: str = "Azione", penale: float = 3.00) -> None:
        super().__init__(id_film, title)
        self.__genere = genere 
        self.__penale = penale 

    def getGenere(self) -> str:
        return self.__genere 
    
    def getPenale(self) -> float:
        return self.__penale 
    
    def calcolaPenaleRitardo(self, giorni: int) -> None:
        if not isinstance(giorni, int) or giorni <= 0:
            raise ValueError("Il numero di giorni deve essere un numero maggiore di 0")
        else:
            return self.getPenale() * giorni 


class Commedia(Film):
    def __init__(self, id_film: int, title: str, genere: str = "Commedia", penale: float = 2.50) -> None:
        super().__init__(id_film, title)
        self.__genere = genere 
        self.__penale = penale 

    def getGenere(self) -> str:
        return self.__genere 
    
    def getPenale(self) -> float:
        return self.__penale 
    
    def calcolaPenaleRitardo(self, giorni: int) -> None:
        if not isinstance(giorni, int) or giorni <= 0:
            raise ValueError("Il numero di giorni deve essere un numero maggiore di 0")
        else:
            return self.getPenale() * giorni 


class Drama(Film):
    def __init__(self, id_film: int, title: str, genere: str = "Drama", penale: float = 2.00) -> None:
        super().__init__(id_film, title)
        self.__genere = genere 
        self.__penale = penale 

    def getGenere(self) -> str:
        return self.__genere 
    
    def getPenale(self) -> float:
        return self.__penale 
    
    def calcolaPenaleRitardo(self, giorni: int) -> float:
        if not isinstance(giorni, int) or giorni <= 0:
            raise ValueError("Il numero di giorni deve essere un numero maggiore di 0")
        else:
            return self.getPenale() * giorni 


    