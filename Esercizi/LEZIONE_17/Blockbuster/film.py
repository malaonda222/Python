from __future__ import annotations


class Film:
    def __init__(self, id_film: int, title: str) -> None:
        self.setId(id_film)
        self.setTitle(title)

    def setId(self, id_film: int) -> None:
        if not isinstance(id_film, int) or id_film < 0:
            raise ValueError("L'ID deve essere un numero intero positivo!")
        else:
            self.__id_film = id_film 
    
    def getId(self) -> int:
        return self.__id_film 

    def setTitle(self, title: str) -> None:
        if not isinstance(title, str) or title.strip() == "":
            raise ValueError("Il titolo deve essere una stringa e non può essere vuota")
        else:
            self.__title = title 

    def getTitle(self) -> str:
        return self.__title 
    
    def isEqual(self, otherFilm: int) -> str:
        if isinstance(otherFilm, Film):
            return self.__id_film == self.__otherFilm
        
    

        


