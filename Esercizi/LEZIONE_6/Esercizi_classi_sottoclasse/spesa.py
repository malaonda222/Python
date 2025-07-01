class Prodotto:
    def __init__(self, nome:str, prezzo:float, quantita:int):
        if not nome.isalpha():
            raise ValueError("Errore. Il nome deve essere composto solo da lettere.")
        self.nome = nome 
        if prezzo <= 0:
            raise ValueError("Errore. Il prezzo deve essere maggiore di 0.")
        self.prezzo = prezzo 
        if quantita < 0:
            raise ValueError("Errore. La quantità deve essere maggiore di 0.")
        self.quantita = quantita 

    def __str__(self):
        return f"Caratteristiche del prodotto:\n{self.nome} - {self.prezzo:.2f} x {self.quantita}"

    def getName(self) -> str:
        return self.nome 
    
    def getPrezzo(self) -> float:
        return self.prezzo 
    
    def getQuantita(self) -> int:
        return self.quantita 
    
class Carrello:
    def __init__(self):
        self.prodotti:list[str] = []

    def aggiungi_prodotto(self, prodotto:Prodotto):
        self.prodotti.append(prodotto)

    def mostra_carrello(self):
        print("I prodotti nel carrello sono:")
        for prodotto in self.prodotti:
            print("-", prodotto)
    
    def totale(self):
        totale = 0
        for prodotto in self.prodotti:
            totale += prodotto.getPrezzo() * prodotto.getQuantita() 
        return totale 
    
    def cerca_prodotto(self, nome:str):
        trovati = [prodotto for prodotto in self.prodotti if prodotto.getName().lower() == nome.lower()]
        if trovati:
            print("Risultato della ricerca:")
            for prodotto in trovati:
                print("Hai cercato:", prodotto)
        else: 
            print("Il prodotto non è presente nel carrello della spesa.")


insalata = Prodotto("Insalata", 1.50, 2)
print(insalata)
yogurt = Prodotto("Yogurt", 1.60, 4)
print(yogurt)
pollo = Prodotto("Pollo", 6.00, 1)
print(pollo)

carrello = Carrello()
carrello.aggiungi_prodotto(insalata)
carrello.aggiungi_prodotto(yogurt)
carrello.aggiungi_prodotto(pollo)
carrello.mostra_carrello()

print(f"Il totale della spesa è {carrello.totale()}\n")
carrello.cerca_prodotto("Panna")
