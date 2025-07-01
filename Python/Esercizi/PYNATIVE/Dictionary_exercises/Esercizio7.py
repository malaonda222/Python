# Check if a value exists in a dictionary
sample_dict = {'a': 100, 'b': 200, 'c': 300}

lista1 = []
for value in sample_dict.values():
    lista1.append(value)
print(lista1)

numero = 200
for i in lista1:
    if i == numero:
        print("Il numero è presente nella lista!")
        trovato = True
    
