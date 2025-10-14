class InventoryManager:
    def __init__(self) -> None:
        self.inventory: dict[str, dict] = {}

    def add_product(self, product_id: str, nome: str, quantita: int, prezzo: float) -> dict|str:
        if product_id in self.inventory:
            print("Errore: prodotto esiste già.")
        else:
            self.inventory[product_id] = {"nome": nome, "quantita": quantita, "prezzo": prezzo}
            return {product_id: self.inventory[product_id]}
        
    def update_quantity(self, product_id: str, nuova_quantita: int) -> dict|str:
        if product_id not in self.inventory:
            print("Errore. Prodotto non trovato.")
        else:
            self.inventory[product_id]["quantita"] = nuova_quantita
            return {product_id: self.inventory[product_id]}
    
    def update_price(self, product_id: str, nuovo_prezzo: float) -> dict|str:
        if product_id not in self.inventory:
            print("Errore. Prodotto non trovato.")
        else:
            self.inventory[product_id]["prezzo"] = nuovo_prezzo
            return {product_id: self.inventory[product_id]}

    def remove_product(self, product_id: str) -> dict|str:
        if product_id not in self.inventory:
            print("Errore. Prodotto non trovato.")
        else:
            rimosso = self.inventory.pop(product_id)
            return {product_id: rimosso}
    
    def list_products(self) -> list[str]:
        return list(self.inventory.keys())
    
    def get_product(self, product_id: str) -> dict|str:
        if product_id not in self.inventory:
            print("Errore. Prodotto non trovato.")
        else:
            return {product_id: self.inventory[product_id]}
        
    def list_products2(self) -> list[str]:
        lista_prodotti = []
        for key in self.inventory.keys():   
            lista_prodotti.append(key)
        return lista_prodotti
    
    def list_products3(self) -> list[str]:
        return [key for key in self.inventory.keys()]