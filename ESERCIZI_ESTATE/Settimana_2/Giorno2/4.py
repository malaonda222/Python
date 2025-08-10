'''Estrai solo le parole con più di 5 lettere.'''

lista_numeri: list = ["erano", "sempre", "insieme"]
print([element for element in lista_numeri if len(element) > 5])

print({element: len(element) for element in lista_numeri})

print({elemento: len(elemento) for elemento in lista_numeri if len(elemento) > 5})