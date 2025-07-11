from __future__ import annotations
from datetime import date

class Atleta:
    def __init__(self, nome: str, cognome: str, record_personale: float) -> None:
        self._nome = nome 
        self._cognome = cognome 
        self._record_personale = record_personale
        self._partecipazioni: list[Partecipazione._link] = []
    
    def nome(self) -> str:
        return self._nome 
    
    def cognome(self) -> str:
        return self._cognome 
    
    def record_personale(self) -> float:
        return self._record_personale 
    
    def partecipazioni(self) -> list[Partecipazione._link]:
        return self._partecipazioni 
    
    def _add_link(self, link: Partecipazione._link):
        self._partecipazioni.append(link)

    def __str__(self) -> str:
        return f"{self.nome()} {self.cognome()} - Record: {self.record_personale()}"
    
class Gara:
    def __init__(self, data: date, luogo: str) -> None:
        self._data = data 
        self._luogo = luogo
        self._lista_partecipanti: list[Atleta] = []
        self._partecipazioni: list[Partecipazione._link] = []

    def data(self) -> date:
        return self._data

    def luogo(self) -> str:
        return self._luogo
    
    def _add_link(self, link: Partecipazione._link):
        self._partecipazioni.append(link)

    def __str__(self) -> str:
        return f"Gara a {self.luogo()} il {self.data()}"
    
class Partecipazione:

    @classmethod
    def add(cls, atleta: Atleta, gara: Gara, risultato: float) -> None:
        link = cls._link(atleta, gara, risultato)
        atleta._add_link(link)
        gara._add_link(link)

    class _link:
        def __init__(self, atleta: Atleta, gara: Gara, risultato: float) -> None:
            self._atleta = atleta
            self._gara = gara 
            self._risultato = risultato 

        def atleta(self) -> Atleta:
            return self._atleta 
        
        def gara(self) -> Gara:
            return self._gara 
        
        def risultato(self) -> float:
            return self._risultato 
        
        def __str__(self):
            return f"{self._atleta.nome()} {self._atleta.cognome()} - Risultato: {self._risultato}"


if __name__ == "__main__":
    atleta1 = Atleta("Usain", "Bolt", 9.58)
    atleta2 = Atleta("Yohan", "Blake", 9.69)

    gara = Gara(date(2025, 11, 12), "Firenze")

    Partecipazione.add(atleta1, gara, 9.60)
    Partecipazione.add(atleta2, gara, 9.70)

    print(f"\n{gara}")
    print("Classifica gara:")
    partecipazioni_ordinate = sorted(
        atleta1.partecipazioni() + atleta2.partecipazioni(),
        key=lambda p: p.risultato()
    )
    for p in partecipazioni_ordinate:
        if p.gara() == gara:
            print(p)
