class Prodotto:
    def __init__(self, nome: str, quantita: int) -> None:
        self.nome = nome 
        self.quantita = quantita 

    def __str__(self) -> str:
        return f"Nome prodotto: {self.nome} - Quantità: {self.quantita}"
    
class Magazzino:
    def __init__(self, nome: str):
        self.nome = nome 
        self.lista_prodotti = []
    
    def aggiungi_prodotto(self, prodotto: Prodotto) -> None:
        self.lista_prodotti.append(prodotto)
        print(f"Prodotto {prodotto} aggiunto alla lista dei prodotti")
    
    def cerca_prodotto(self, nome: str) -> Prodotto:
        for prodotto in self.lista_prodotti:
            if nome == prodotto.nome:
                return f"Prodotto: {prodotto}"
        return f"Il prodotto {nome} non è stato trovato"
        
    def verifica_disponibilita(self, nome: str) -> str:
        for prodotto in self.lista_prodotti:
            if nome == prodotto.nome:
                if prodotto.quantita > 0:
                    return f"Prodotto '{nome}' disponibile: {prodotto.quantita} unità"
                else:
                    return f"Il prodotto '{prodotto.nome}' non è disponibile"
        return f"Il prodotto '{nome}' non si trova in magazzino"
    

prodotto1 = Prodotto("Carta Igienica", 10)
prodotto2 = Prodotto("Spazzolino", 2)
prodotto3 = Prodotto("Dentifricio", 0)
print(prodotto1)
print(prodotto2)
print(prodotto3)

magazzino = Magazzino("Bino")
magazzino.aggiungi_prodotto(prodotto1)
magazzino.aggiungi_prodotto(prodotto3)
print(magazzino.cerca_prodotto("Spazzolino"))
print(magazzino.verifica_disponibilita("Dentifricio"))



