'''Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un 
nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, ma scontati del 10%.'''

def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    dict_nuovo = {}
    sconto = 0.1
    for key, value in prodotti.items():
        if value > 20:
            sconto_assoluto = value * sconto
            prezzo_scontato = value - sconto_assoluto
            dict_nuovo[key] = prezzo_scontato
    return dict_nuovo
