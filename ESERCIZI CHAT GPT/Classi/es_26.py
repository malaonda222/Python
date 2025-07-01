'''Classe Playlist con:
Attributi: nome, brani (lista)
Metodi:
aggiungi_brano(titolo)
rimuovi_brano(titolo)
mostra_brani() → stampa la lista'''

class Playlist:
    def __init__(self, nome:str):
        self.nome = nome 
        self.brani = []
    
    def aggiungi_brano(self, titolo:str):
        self.brani.append(titolo)
        print(f"{titolo} è stato aggiunto alla playlist {self.nome}.")
    
    def rimuovi_brano(self, titolo: str):
        if titolo in self.brani:
            self.brani.remove(titolo)
            print(f"Il brano {titolo} è stato rimosso dalla playlist {self.nome}.")
        else:
            print(f"Il brano {titolo} non è stato trovato nella playlist {self.nome}.")
        
    def mostra_brani(self):
        if not self.brani:
            print("La playlist è vuota.")
        else: 
            for i, brano in enumerate(self.brani, start=1):
                print(f"{i}. {brano}")

playlist1 = Playlist("Chill")
playlist1.aggiungi_brano("Sottomarini")
playlist1.aggiungi_brano("Remember me")
playlist1.aggiungi_brano("Ciao")
playlist1.aggiungi_brano("Tre volte")
playlist1.mostra_brani()