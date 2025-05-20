class Prodotto:
    def __init__(self, nome: str, prezzo: float, quantita: int):
        self.nome = nome 
        self.prezzo = prezzo 
        self.quantita = quantita 

    def valore_totale(self):
        return self.prezzo * self.quantita 
    
    def vendi(self, qta: int):
        if qta <= 0:
            print("Impossibile scalare la quantità.")
        elif qta > self.quantita: 
            print(f"Errore, c'è solo {self.quantità} unità disponibili di {self.nome}.")
        else:
            self.quantità -= qta
            print(f"Venduta {qta} unità di {self.nome}. Quantità rimasta: {self.quantita}")    
