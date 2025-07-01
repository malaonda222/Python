dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

#si sovrascrive il dict1 (diventa l'unione dei due dizionari)
dict1.update(dict2)
print(dict1)

#si crea un nuovo dizionario (unione dei dict1 e dict2)
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)

new_dict = dict1 | dict2
print(new_dict)