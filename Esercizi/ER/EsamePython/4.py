import uuid
'''
Sistema E-commerce
Progetta e implementa un semplice sistema e-commerce in Python, organizzato attorno a tre classi principali: Product, ShoppingCart e Shop.
Ogni classe deve essere chiara nel proprio scopo e ogni funzione deve essere documentata con responsabilità ben definite.

Classe Product
Rappresenta un singolo prodotto venduto nel negozio online.
Ogni prodotto ha informazioni uniche e uno stock che ne regola la disponibilità.

Attributi
    product_id: str — Identificatore unico del prodotto nello shop (esempio: "SKU1234").
    Serve per distinguere ogni articolo.
    name: str — Nome del prodotto (esempio: "Mouse Wireless Logitech").
    price: float — Prezzo unitario del prodotto in euro (ad esempio 29.90).
    stock: int — Quantità attualmente disponibile a magazzino per il prodotto.

Metodi
    update_stock(quantity: int) -> None
    Aggiorna la quantità disponibile del prodotto.
    Se il parametro è positivo la quantità viene aumentata, se negativo viene diminuita.
    Non restituisce nulla.

    is_available(quantity: int) -> bool
    Controlla se il prodotto ha almeno la quantità richiesta disponibile (utile per le vendite).
    Ritorna True se lo stock è sufficiente, False altrimenti.


Classe ShoppingCart
Questa classe simula il carrello di un utente, che può contenere più prodotti con relative quantità.
 Opera come contenitore temporaneo fino al momento del pagamento.

Attributi
    items: dict[str, int] — Dizionario che associa ogni product_id alla quantità richiesta da acquistare da parte dell’utente.
    Esempio: { 'SKU1234': 2, 'SKU5678': 1 }.


Metodi
    add_item(product: Product, quantity: int) -> str
    Tenta di aggiungere il prodotto al carrello nella quantità richiesta.
    Se la quantità disponibile non è sufficiente, restituisce un messaggio di errore.
    Se l’aggiunta va a buon fine, aggiorna lo stock del prodotto (diminuisce di quantity) e ritorna un messaggio di conferma.

    remove_item(product_id: str) -> str
    Rimuove dal carrello il prodotto corrispondente al product_id.
    Se il prodotto era presente, lo elimina e restituisce conferma; se non era presente, restituisce un messaggio di errore.

    get_total(products: dict[str, Product]) -> float
    Calcola e ritorna la somma totale degli articoli nel carrello, moltiplicando il prezzo unitario per la quantità di ogni prodotto.
    Ha bisogno del dizionario dei prodotti per accedere ai prezzi.

    clear() -> None
    Svuota tutto il carrello, rimuovendo tutti i prodotti e le relative quantità.'''

'''
Classe Shop
Attributi
    products: dict[str, Product]
    Mappa ogni product_id a un oggetto Product, rappresentando l’intero inventario del negozio.

    carts: dict[str, ShoppingCart]
    Mappa ogni carrello (identificato da un cart_id, es. "cart123") all’oggetto ShoppingCart corrispondente.
    Così si gestiscono più clienti contemporaneamente.


Metodi
    add_product(product: Product) -> str
    Aggiunge un nuovo prodotto al negozio.
    Se il product_id è già presente, non aggiunge il prodotto e restituisce un messaggio di errore;
    altrimenti, aggiunge il nuovo prodotto e ritorna una stringa di conferma.

    remove_product(product_id: str) -> str
    Rimuove il prodotto col dato product_id dall’inventario.
    Restituisce conferma se l’operazione ha successo o un errore se il prodotto non esiste.

    create_cart() -> str
    Crea un nuovo carrello della spesa, genera un nuovo cart_id (può usare ad esempio uuid),
    lo inserisce nella mappa carts e ritorna il suo id.

    checkout(cart_id: str) -> float | str
    Conclude l’acquisto per il carrello identificato da cart_id.
    Se tutti i prodotti nel carrello sono effettivamente disponibili negli stock,
    calcola il totale, aggiorna definitivamente le giacenze e svuota il carrello.
    Se manca disponibilità per uno o più prodotti durante questa verifica,
    restituisce un messaggio di errore (ad esempio specificando quali oggetti non sono disponibili)
    e non conclude l’acquisto.

'''

class Product:
    def __init__(self, product_id: str, name: str, price: float, stock: int) -> None:
        self.product_id: str = product_id
        self.name: str = name 
        self.price: float = price 
        self.stock: int = stock 
    
    def update_stock(self, quantity: int) -> None:
        self.stock += quantity 
        if self.stock < 0:
            self.stock = 0
    
    def is_available(self, quantity: int) -> bool:
        if self.stock >= quantity:
            return True 
        else:
            return False 
        
class ShoppingCart:
    def __init__(self) -> None:
        self.items: dict[str, int] = {}

    def add_item(self, product: Product, quantity: int) -> str:        
        if not product.is_available(quantity):
            return "Errore. Stock non sufficiente"
        
        if product.product_id in self.items:
            self.items[product.product_id] += quantity 
        else:
            self.items[product.product_id] = quantity
        product.update_stock(-quantity)
        return "Prodotto aggiunto al carrello"
    
    def remove_item(self, product_id: str) -> str:
        if product_id not in self.items:
            return "Errore. Prodotto non presente nel carrello"
        else:
            del self.items[product_id]
            return "Prodotto eliminato dal carrello"
    
    def get_total(self, products: dict[str, Product]) -> float:
        somma_totale = 0.0
        for product_id, quantity in self.items.items():
            if product_id in products:
                somma_totale += products[product_id].price * quantity
        return somma_totale
    
    def clear(self) -> None:
        self.items.clear()
    
class Shop:
    def __init__(self) -> None:
        self.products: dict[str, Product] = {}
        self.carts: dict[str, ShoppingCart] = {}
    
    def add_product(self, product: Product) -> str:
        if product.product_id in self.products:
            return "Errore. Product ID già presente."
        else:
            self.products[product.product_id] = product 
            return "Prodotto aggiunto con successo."
    
    def remove_product(self, product_id: str) -> str:
        if product_id in self.products:
            del self.products[product_id]
            return "Prodotto eliminato con successo."
        else:
            return "Errore. Il prodotto non esiste."
    
    def create_cart(self) -> str:
        nuova_cart = str(uuid.uuid4())
        self.carts[nuova_cart] = ShoppingCart()
        return nuova_cart
    
    def checkout(self, cart_id: str) -> float|str:
        if cart_id not in self.carts:
            return "Errore. Cart ID non presente."
        else:
            totale = 0.0
            non_disponibili = []
            cart = self.carts[cart_id]
            for product_id, quantity in cart.items.items():
                if product_id not in self.products or not self.products[product_id].is_available(quantity):
                    non_disponibili.append(product_id)
            if non_disponibili:
                return f"Errore. Prodotti non disponibili: {non_disponibili}"
            totale = cart.get_total(self.products)
            cart.clear()
            return totale 
        


