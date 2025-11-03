'''Scrivi una funzione che accetti un dizionario di prodotti con i prezzi 
e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo 
superiore a 20, ma scontati del 10%.'''

def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    new_dict: dict = {}
    for key, value in prodotti.items():
        if value > 20:
            prodotto_scontato = round(value * 0.90, 2)
            new_dict[key] = prodotto_scontato
    return new_dict

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))