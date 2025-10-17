'''Ordinare prodotti per prezzo (crescente)
Hai una lista di dizionari con nome e prezzo. Ordina i prodotti dal meno costoso al più 
costoso usando bubble sort, senza usare sorted().'''

# versione con bubble sort
def ordina_prodotti(prodotti: list[dict[str, float]]) -> list[tuple]:
    new_list = []
    for prodotto in prodotti:
        nome = prodotto["nome"]
        prezzo = prodotto["prezzo"]
        new_list.append((nome, prezzo))
    
    n = len(new_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if new_list[j][1] > new_list[j+1][1]:
                new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
    return new_list

# versione con lambda 
def ordina_prodotti1(prodotti: list[dict[str, float]]) -> list[tuple]:
    new_list = []
    for prodotto in prodotti:
        nome = prodotto["nome"]
        prezzo = prodotto["prezzo"]
        new_list.append((nome, prezzo))
    return sorted(new_list, key=lambda x:x[1])


prodotti = [
    {"nome": "Mouse", "prezzo": 25.0},
    {"nome": "Monitor", "prezzo": 150.0},
    {"nome": "Tastiera", "prezzo": 45.0}
]

print(ordina_prodotti(prodotti))
print(ordina_prodotti1(prodotti))

