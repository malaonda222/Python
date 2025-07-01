class Prodotto:
    def __init__(self, nome:str, quantità: int):
        self.nome = nome
        self.quantità = quantità 
    
    def __str__(self):
        return f"Prodotto: {self.nome}\nQuantità: {self.quantità}"

class Magazzino:
    def __init__ (self):
        self.prodotti = {}

    def aggiungi_prodotto(self, prodotto: Prodotto):
        if prodotto.nome in self.prodotti:
            self.prodotti[prodotto.nome].quantità += prodotto.quantità
            return f"La quantità del prodotto è stato aggiornata."
        else:
            self.prodotti[prodotto.nome] = prodotto
            return f"Il prodotto è stato aggiunto al magazzino."

    def cerca_prodotto(self, nome: str):
        if not isinstance(nome, str):
            print("Inserisci un nome valido.")
        if nome in self.prodotti:
            return self.prodotti[nome]
        else:
            print(f"Prodotto non presente in magazzino.")
            
    def verifica_disponibilità(self, nome: str):
        prodotto = self.cerca_prodotto(nome)
        if prodotto and prodotto.quantità >= 0:
            return f"Il prodotto {nome} è disponibile in quantità: {prodotto.quantità}."
        else:
            return f"Il prdotto {nome} non è disponibile in magazzino."
        
magazzino = Magazzino()
prodotto1 = Prodotto("Trapano", 2)
prodotto2 = Prodotto("Chiodo", 100)
print(prodotto1)
print(prodotto2)
print(magazzino.aggiungi_prodotto(prodotto1))
print(magazzino.aggiungi_prodotto(prodotto2))
print(magazzino.cerca_prodotto("Trapano"))
print(magazzino.cerca_prodotto("Martello"))
print(magazzino.verifica_disponibilità("Trapano"))
print(magazzino.verifica_disponibilità("Martello"))


