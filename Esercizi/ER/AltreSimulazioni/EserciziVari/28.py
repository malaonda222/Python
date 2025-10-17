'''
Esercizio - Top Spending Customers
Tema: Ordinamento e selezione di dati aggregati
Obiettivo: Individuare i clienti che hanno speso di più
 
Nome dell’esercizio: Top Spending Customers
Traccia:
Scrivi una funzione chiamata top_spending_customers che riceve una lista di dizionari contenenti "cliente" e "totale".
La funzione deve restituire una lista di tuple ordinate in ordine decrescente per totale speso, 
dove ogni tupla è nella forma (cliente, totale_speso).
 
Esempio di input:
[
    {"cliente": "Anna", "totale": 50},
    {"cliente": "Marco", "totale": 30},
    {"cliente": "Luca", "totale": 75}
]
 
Esempio di output:
[("Luca", 75), ("Anna", 50), ("Marco", 30)]
'''

def top_spending_cutomers(orders: list[dict[str, float]]) -> list[tuple]:
    lista_tuple = []
    for order in orders:
        cliente = order["cliente"]
        totale = order["totale"]
        lista_tuple.append((cliente, totale))

    n = len(lista_tuple)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista_tuple[j][1] < lista_tuple [j+1][1]:
                lista_tuple[j], lista_tuple[j+1] = lista_tuple[j+1], lista_tuple[j]
    return lista_tuple
        
    # return sorted(lista_tuple, key = lambda x: x[1], reverse=True)

ordini = [
    {"cliente": "Anna", "totale": 50},
    {"cliente": "Marco", "totale": 30},
    {"cliente": "Luca", "totale": 75}
]
print(top_spending_cutomers (ordini))