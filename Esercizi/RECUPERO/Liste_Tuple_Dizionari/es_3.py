'''3) Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali.
'''

def dizionario_prodotti(dict_1: dict) -> dict:
    dizionario_prodotti_minori_50 = {}
    for key, value in dict_1.items():
        if value < 50:
            dizionario_prodotti_minori_50[key] = round(value * 1.1, 2)
        
    return dizionario_prodotti_minori_50

dict_1 = {"a": 51, "b": 49, "c":75, "d": 53, "e": 25}
nuovo_dict = dizionario_prodotti(dict_1)
print(nuovo_dict)


def filter_product_dict(dict_1: dict) -> dict:
    dict_4: dict = {}
    for key, value in dict_1.items():
        if value > 50:
            continue
        else:
            dict_4[key] = round(value + value * 0.10, 2)

    return dict_4

dict_1 = {"cia": 51, "bau": 49, "col":75, "da": 53, "em": 25}
dict_out: dict = filter_product_dict(dict_1)
print(f"La soluzione dell'esercizio 3 è: {dict_out}")


