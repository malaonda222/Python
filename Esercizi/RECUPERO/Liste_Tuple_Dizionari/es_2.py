'''2) Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
classifichi i numeri in liste separate per numeri positivi e negativi.'''


def classifica(lista_1: list[int]) -> dict:
    dizionario = {"positivo": [], "negativo": []}
    
    for i in lista_1:
        if i >= 0:
            dizionario["positivo"].append(i)
        else:
            dizionario["negativo"].append(i)
    return dizionario

lista_1 = (-3, 5, -9, 7, 2)
print(classifica(lista_1))


def filter_positive_negative(list_1: list) -> dict:
    dict_1 = {"positivi": [], "negativi": []}
    for element in list_1:
        if element >= 0:
            dict_1["positivi"].append(element)
        else:
            dict_1["negativi"].append(element)
    return dict_1

list_2: list = [2, -5, 8, 6363, -10, -80]
dict_2: dict = filter_positive_negative(list_2)
print(f"La soluzione dell'esercizio 2 è: {dict_2}")
