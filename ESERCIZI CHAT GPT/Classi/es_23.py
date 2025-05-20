class Articolo:
    def __init__(self, nome:str, quantità:int):
        self.nome = nome 
        self.quantità = quantità 
    
    def __str__(self):
        return f"Articolo: {self.nome} - Quantità: {self.quantità}"
    
class ListaSpesa:
    def __init__(self):
        self.lista = []

    def aggiungi_articolo(self, nome:str, quantità:int):
        for articolo in self.lista:
            if articolo.nome.lower() in nome.lower():
                articolo.quantità += quantità 
                print(f"La quantità del prodotto {nome} è stata aggiornata.")
                return 
        nuovo = Articolo(nome, quantità)
        self.lista.append(nuovo)
        print(f"Il prodotto {nuovo} è stato aggiunto alla lista.")
    
    def rimuovi_articolo(self, nome:str):
        for articolo in self.lista:
            if articolo.nome.lower() in nome.lower():
                self.lista.remove(articolo)
                print(f"L'articolo \"{nome}\" è stato rimosso dalla lista della spesa.")
        print(f"Articolo non presente nella lista.")

    def stampa_lista(self):
        print("--- Lista della spesa ---")
        if not self.lista:
            print("La lista è vuota.")
        for articolo in self.lista:
            print(f" - {articolo}")

lista = ListaSpesa()
lista.aggiungi_articolo("Pane", 2)
lista.aggiungi_articolo("Latte", 1)
lista.aggiungi_articolo("Uova", 6)
lista.aggiungi_articolo("Pane", 1)

lista.rimuovi_articolo("Latte")
lista.rimuovi_articolo("Acqua")

lista.stampa_lista()


