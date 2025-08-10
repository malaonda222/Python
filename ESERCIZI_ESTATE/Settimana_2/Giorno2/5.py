'''Crea un dizionario da una lista con comprehension.'''

lista:list = [("a", 1), ("b", 2), ("c", 3)]

print({key: value for key, value in lista})

dizionario: dict = {key: value for key, value in lista if value >= 2}
print(dizionario)


