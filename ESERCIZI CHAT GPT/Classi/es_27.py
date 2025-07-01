'''Classe Prodotto:
Attributi: nome, prezzo
Classe Negozio:
Attributo: lista di prodotti 
Metodi:
aggiungi_prodotto(prodotto) 
totale_prodotti() → quanti prodotti ci sono
valore_totale() → somma dei prezzi
mostra_prodotti()'''

class Prodotto:
    def __init__(self, nome: str, prezzo: float):
        self.nome = nome 
        self.prezzo = prezzo 

    def __str__(self):
        return f"Prodotto {self.nome}; Prezzo: euro {self.prezzo:.2f}."

class Negozio:
    def __init__(self):
        self.prodotti = []

    def aggiungi_prodotto(self, prodotto: str):
        self.prodotti.append(prodotto)
        print(f"Il prodotto {prodotto.nome} è stato aggiunto al negozio.")

    def totale_prodotti(self):
        return len(self.prodotti)
    
    def valore_totale(self):
        totale = sum(prodotto.prezzo for prodotto in self.prodotti)
        print(f"Il prezzo totale dei prodotti è: euro {totale}")
    
    def mostra_prodotti(self):
        if not self.prodotti:
            print(f"La lista è vuota.")
        else:
            for prodotto in self.prodotti:
                print(f"  -  {prodotto}")


p1 = Prodotto("Tastiera", 39.90)
p2 = Prodotto("Mouse", 19.99)
p3 = Prodotto("Monitor", 149.00)

negozio = Negozio()
negozio.aggiungi_prodotto(p1)
negozio.aggiungi_prodotto(p2)
negozio.aggiungi_prodotto(p3)
negozio.valore_totale()

negozio.mostra_prodotti()

    
        

    
