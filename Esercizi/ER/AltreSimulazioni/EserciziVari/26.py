'''Descrizione:
Scrivi una funzione chiamata summarize_orders che riceve in ingresso una lista di dizionari. 
Ogni dizionario rappresenta un ordine e contiene le chiavi "cliente" e "totale".
La funzione deve restituire una stringa dove per ogni cliente compare il totale speso, 
formattato come:
nome_cliente: €totale
Gli elementi devono essere separati da una virgola.'''

def summarize_orders(orders: list[dict[str, float]]) -> str:
    formattato = [f" {order['cliente']}: € {order['totale']}" for order in orders]
    return ",".join(formattato)

print(summarize_orders([
    {"cliente": "Anna", "totale": 35.5},
    {"cliente": "Marco", "totale": 42.0},
    {"cliente": "Luca", "totale": 15.75}
]))
