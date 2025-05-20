'''Carrello degli acquisti e-commerce :

Crea una funzione che definisca un prodotto con un nome, un prezzo e una 
quantità.
Creare funzioni che gestiscano il carrello, consentendo all'utente 
di aggiungere, rimuovere e visualizzare i prodotti nel carrello.
Crea una funzione che calcoli il totale del carrello e applichi eventuali 
sconti o tasse.
Crea una funzione per stampare un riepilogo dettagliato del carrello, 
inclusi prodotti e totali.
Implementare un ciclo for per scorrere gli articoli nel carrello e stampare 
informazioni dettagliate su ciascun prodotto e il totale.'''

from typing import Any

def prodotto(nome: str, prezzo: float, quantità: int) -> dict[str, Any]:
    return {
        "nome": nome,
        "prezzo": prezzo,
        "quantità": quantità
    }

def aggiungere_prodotto(carrello: list[dict[str, Any]], product: dict[str, Any]) -> None:
    carrello.append(product) 

def rimuovi_prodotto(carrello: list[dict[str, Any]], nome_prodotto: str) -> list[dict[str, Any]]:
    updated_carrello: list[dict[str, Any]] = []
    for product in carrello:
        if product["nome"] != nome_prodotto:
            updated_carrello.append(nome_prodotto)
    return updated_carrello

def visualizza_prodotti(carrello: list[dict[str, Any]]) -> None:
    print("La shopping card contiene: ")
    for product in carrello:
        print(f" - {product["name"]}: {product["quantità"]} unità al prezzo di {product["prezzo"]} ciascuno:")

def calcolo_totale(carrello: list[dict[str, Any]], discount_rate: float=0.20) -> dict[str, float]:
    subtotal: float = sum(product['price'] * product['quantity'] for product in carrello)
    discount: float = discount_rate
    tax: float = 0.22  # VAT of 22%
    
    discounted_total: float = subtotal * (1 - discount)
    total: float = discounted_total * (1 + tax)
    
    return {
        "subtotal": subtotal,
        "discount": discount * 100,  # As a percentage
        "tax": tax * 100,            # As a percentage
        "total": total
    }

def print_summary(carrello: list[dict[str, Any]]) -> None:
    visualizza_prodotti(carrello)
    print("Riassunto dettagliato: ")

    if not carrello:
        print("La lista è vuota.")
    for product in carrello:
        totals: dict[str, float] = calcolo_totale(carrello)
        print("Totali")
        print(f"Subtotali: {totals["subtotal"]}")
        print(f"Discount Applied: {totals['discount']}%")
        print(f"Tax: {totals['tax']}%")
        print(f"Final Total: €{round(totals['total'], 2)}")