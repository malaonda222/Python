'''Filtra un dizionario per tenere solo i valori > 10'''

diz: dict = {"a": 10, "b": 333, "c": 90, "d": 2}
new_dict = {}
for key, value in diz.items():
    if value > 10:
        new_dict[key] = value 
print(new_dict)

diz: dict = {"a": 10, "b": 333, "c": 90, "d": 2}
print({key: value for key, value in diz.items() if value > 10})
