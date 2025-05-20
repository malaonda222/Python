from abc import ABC, abstractmethod

class StrumentoMusicale(ABC):
    @abstractmethod
    def suona(self) -> None:
        pass 

class Chitarra(StrumentoMusicale):
    def suona(self):
       print(f"Strimpello la chitarra.")
    

class Pianoforte(StrumentoMusicale):
    def suona(self):
        print(f"Suono il pianoforte.")


def esibizione(strumento: StrumentoMusicale):
    strumento.suona()


c: Chitarra = Chitarra()
p: Pianoforte = Pianoforte()
esibizione(c)
esibizione(p)