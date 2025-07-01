def positivo_negativo(lista: list[int|float]) -> dict:
    d: dict = {}
    numeri_positivi = []
    numeri_negativi = []
    for num in lista:
        if num >= 0:
            numeri_positivi.append(num)
        else:
            numeri_negativi.append(num)
    d["Numeri positivi"] = numeri_positivi
    d["Numeri negativi"] = numeri_negativi 
    return d




def pos_neg(lista: list[int]) -> dict:
    diz2: dict = {"numeri_positivi": [], "numeri_negativi": []}

    for i in lista:
        if i >= 0:
            diz2["numeri_positivi"].append(i)
        else:
            diz2["numeri_negativi"].append(i)
    return diz2 


lista1 = [1, 5, 2, 99, -3, 6, -99]
print(positivo_negativo(lista1))
print(pos_neg(lista1))