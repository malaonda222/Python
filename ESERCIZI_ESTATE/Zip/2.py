'''Usa zip() per associare chiavi e valori.
Crea un dizionario che associ ogni prodotto al suo prezzo.
Stampa ogni voce del dizionario in formato: "penna: 1.2 euro"'''

prodotti = ["penna", "quaderno", "gomma"]
prezzi = [1.2, 2.5, 0.8]
dizionario = zip(prodotti, prezzi)

for prodotto, prezzo in dizionario:
    print(f"{prodotto}: {prezzo} euro")

dizionario_nuovo = dict(zip(prodotti, prezzi))
print(dizionario_nuovo)