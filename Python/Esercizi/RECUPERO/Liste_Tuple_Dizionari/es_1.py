'''1) Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
la chiave è già presente, somma il valore al valore già associato alla chiave.
'''

def convert_list_of_tuple_to_dict(list_1: list[tuple]) -> dict:
    dizionario = {}
    for key, value in list_1.items():
        if key not in dizionario:
            dizionario[key] = value 
        else:
            dizionario[key] += value
    return dizionario



def convert(list_1: list[tuple]) -> dict:
    diz = {}
    for element in list_1:
        key, value = element[0], element[1]
        if key in diz:
            diz[key] += value 
        else:
            diz[key] = value 
    return diz 

lista_1: list[tuple] = [(0, "valore1"), (1, "valore2")]
dict_2: dict = convert(list_1=lista_1)

print(dict_2)




