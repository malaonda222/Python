'''Crea un dizionario da due liste: ["a", "b"], [1, 2] → {"a":1, "b":2}'''

lista1: list = ["a", "b"]
lista2: list = [1, 2]

dizionario: dict = {}
for i in range(len(lista1)):
    dizionario.update({lista1[i] : lista2[i]}) 
    #oppure dizionario[lista1[i]] = lista2[i]
    #oppure dizionario : dict = dict(zip(lista1, lista2))
print(dizionario)

