'''
Esercizio - Group Orders by Customer
Tema: Raggruppamento e somma di valori in una lista di dizionari
Obiettivo: Calcolare il totale speso da ciascun cliente sommando più ordini
 
Nome dell’esercizio: Group Orders by Customer
Traccia:
Scrivi una funzione chiamata group_orders_by_customer che riceve in ingresso una lista di dizionari.
Ogni dizionario rappresenta un ordine e contiene le chiavi "cliente" e "totale".
 
La funzione deve restituire un dizionario in cui le chiavi sono i nomi dei clienti e i valori sono la somma totale dei loro ordini.
Esempio di input:
[
    {"cliente": "Anna", "totale": 20.0},
    {"cliente": "Marco", "totale": 35.5},
    {"cliente": "Anna", "totale": 15.0}
]
 
Esempio di output:
{"Anna": 35.0, "Marco": 35.5}
'''

def group_orders_by_customer(orders: list[dict[str, float]]) -> dict:
    new_dict = {}
    for order in orders:
        cliente = order["cliente"]
        totale = order["totale"]
        if cliente in new_dict:
            new_dict[cliente] += totale 
        else:
            new_dict[cliente] = totale
    return new_dict


def group_orders_by_customer2(orders: list[dict[str, float]]) -> dict:
    return {f"{order['cliente']}: {order['totale']}" for order in orders}


esempio = [
    {"cliente": "Anna", "totale": 20.0},
    {"cliente": "Marco", "totale": 35.5},
    {"cliente": "Anna", "totale": 15.0}
]

print(group_orders_by_customer(esempio))
print(group_orders_by_customer2(esempio))
