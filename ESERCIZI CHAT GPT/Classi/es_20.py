class Prodotto:
    def __init__(self, name:str, price:float):
        self.name = name
        self.price = price 
    
    def __str__(self):
        return f"{self.name}: euro {self.price:.2f}"

class Carrello:
    def __init__(self):
        self.prodotti = []

    def aggiungi_prodotto(self, prodotto:str):
        self.prodotti.append(prodotto)
        print(f"Aggiunto {prodotto.name} - euro {prodotto.price:.2f} al carrello della spesa.")
    
    def calcola_totale(self):
        if not self.prodotti:
            return 0
        totale = 0
        for prodotto in self.prodotti:
            totale += prodotto.price
        return totale 
    
    def applica_sconto_10(self):
        totale = self.calcola_totale()
        if totale > 100:
            totale *= 0.9
        return totale 
    
    def mostra_carrello(self):
        print("\n---Carrello---")
        for p in self.prodotti:
            print(p)
        print(f"Totale senza sconto: euro {self.calcola_totale():.2f}.")
        print(f"Totale con sconto (se applicabile): euro {self.applica_sconto_10():.2f}.")
    
p1 = Prodotto("Divano", 1000.00)
p2 = Prodotto("PC", 699.00)
p3 = Prodotto("Cuscino", 24.99)

carrello = Carrello()
carrello.aggiungi_prodotto(p1)
carrello.aggiungi_prodotto(p2) 
carrello.aggiungi_prodotto(p3) 
carrello.applica_sconto_10()
carrello.mostra_carrello()
