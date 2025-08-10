'''Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un 
nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, ma scontati del 10%.'''

def filtra_prodotti(dizionario_prodotti: dict[str, float]) -> dict[str]:
    nuovo_dizionario = {}
    for key, value in dizionario_prodotti.items():
        if value > 20:
            sconto = value * 0.10
            prodotto_scontato = value - sconto 
            nuovo_dizionario[key] = prodotto_scontato
    return nuovo_dizionario


print(filtra_prodotti({"televisione": 2000, "pc": 900, "divano": 50, "carta regalo": 12}))

        