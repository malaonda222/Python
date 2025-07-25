'''Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un 
nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, ma scontati del 10%.'''

def prodotti(prodotti: dict[list[str, int]]) -> dict[str, int]:
    new_dict = {}
    for key, value in prodotti.items():
        if value > 20:
            sconto = value * 0.10
            prodotto_scontato = value - sconto 
            new_dict[key] = prodotto_scontato

    return new_dict

prodott = {"tv": 10, "pc": 33, "tavolo": 25}
print(prodotti(prodott))