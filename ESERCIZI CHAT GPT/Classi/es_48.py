from abc import ABC, abstractmethod

class Animale:
    def __init__(self, nome: str, specie: str, eta: int) -> None:
        self.setNome(nome)
        self.setSpecie(specie)
        self.setEta(eta)

    def setNome(self, nome: str) -> None:
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Errore. Il nome deve essere una stringa")
        self._nome = nome 
    
    def setSpecie(self, specie: str) -> None:
        if not isinstance(specie, str) or not specie.strip():
            raise ValueError("Errore. La specie deve essere una stringa")
        self._specie = specie 
    
    def setEta(self, eta: int) -> None:
        if not isinstance(eta, int):
            raise ValueError("Errore. L'età deve essere un numero intero")
        self._eta = eta 
        
    def nome(self) -> str:
        return self._nome 
    
    def specie(self) -> str:
        return self._specie 
    
    def eta(self) -> int:
        return self._eta 
    
    @abstractmethod
    def verso(self) -> str:
        pass 

class Leone(Animale):
    def __init__(self, nome: str, specie: str, eta: int) -> None:
        super().__init__(nome=nome, specie=specie, eta= eta)

    def verso(self) -> str:
        return "Arrrrrghh"

class Elefante(Animale):
    def __init__(self, nome: str, specie: str, eta: int) -> None:
        super().__init__(nome=nome, specie=specie, eta= eta)

    def verso(self) -> str:
        return "Pffffffrrr"
    
class Scimmia(Animale):
    def __init__(self, nome: str, specie: str, eta: int) -> None:
        super().__init__(nome=nome, specie=specie, eta=eta)

    def verso(self) -> str:
        return "Aaaaaaaaaa"
    
class Zoo:
    def __init__(self):
        self.lista_animali: list[Animale] = []
    
    def aggiungi_animale(self, animale: Animale):
        self.lista_animali.append(animale)
    
    def stampa_tutti_versi(self):
        for animale in self.lista_animali:
            print(f"- {animale.nome()} (Specie: {animale.specie()} - Età: {animale.eta()}) fa il seguente verso: \"{animale.verso()}\"")
    
    def eta_media(self):
        if not self.lista_animali:
            raise ValueError("Nessun animale nello zoo")
        else:
            somma_eta = 0
            for animale in self.lista_animali:
                somma_eta += animale.eta()
            return f"{(somma_eta / len(self.lista_animali)):.2f}"
        
if __name__ == "__main__":
    zoo: Zoo = Zoo()
    zoo.aggiungi_animale(Leone("Mino", "Panthera leo", 5))
    zoo.aggiungi_animale(Scimmia("George", "Cebus capucinus", 3))
    zoo.aggiungi_animale(Elefante("Dumbo", "Elephas maximus", 9))
    print()
    print("Versi di tutti gli animali: ")
    zoo.stampa_tutti_versi()
    print()
    print(f"Età media degli animali dello zoo: {zoo.eta_media()}")