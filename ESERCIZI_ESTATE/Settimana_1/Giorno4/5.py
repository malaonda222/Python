'''Ordina un dizionario per valore'''

# dizionario: dict = {"a": 3, "b": 2, "c": 1}
# for key, value in dizionario.items():
#     valori_ordinati = sorted(value for value in dizionario.values())
#     dizionario.update(valori_ordinati)
# print(dizionario)

dizionario: dict = {"a": 3, "b": 2, "c": 1}
listainvertita = [(v, k) for k, v in dizionario.items()]
listainvertita.sort()
dizionario_ordinato: dict = {k: v for v, k in listainvertita}
print(dizionario_ordinato)