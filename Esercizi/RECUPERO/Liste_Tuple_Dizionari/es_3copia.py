def modifica_prezzo(diz: dict[str, float]) -> dict:
    new_dict = {}
    for key, value in diz.items():
        if value < 50: 
            new_value = value + (value*0.10)
            new_dict[key] = f"{new_value:.2f}"
    return new_dict

my_dict = {"pizza": 20, "TV": 55, "PC": 190, "Poltrona": 300}
print(modifica_prezzo(my_dict))




def modifica_prezzo(diz: dict[str, float]) -> dict:
    new_dict1 = {}
    for key, value in diz.items():
        if value < 50: 
            new_dict1[key] = round(value + value*0.10, 2)
    return new_dict1

prova = {"pizza": 10, "TV": 49, "PC": 190, "Poltrona": 33}
print(modifica_prezzo(prova))