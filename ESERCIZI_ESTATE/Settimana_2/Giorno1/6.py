'''uso di map'''

a = ["a", "b", "c"]
maiuscole = list(map(str.upper, a))
print(maiuscole)

a = ["a", "b", "c"]
minuscole = tuple(map(str.lower, a))
print(minuscole)

a = ["a", "b", "c"]
maiuscole2 = list(map(lambda x:x.upper(), a))
print(maiuscole2)

a = ["a", "b", "c"]
minuscole2 = list(map(lambda x: x.lower(), a))
print(minuscole2)

numeri = [1, 2, 5, 4, 10, 90, 5]
numeri_pari = list(map(lambda numero: numero % 2 == 0, numeri))
print(numeri_pari)

numeri = [1, 2, 5, 4, 10, 90, 5]
numeri_dispari = list(map(lambda numero: numero % 3 == 0, numeri))
print(numeri_dispari)

numeri = [1, 2, 5, 4, 10, 90, 5]
print(any(numero > 20 for numero in numeri))

numeri = [1, 2, 5, 4, 10, 90, 5]
print(all(numero % 3 == 0 for numero in numeri))