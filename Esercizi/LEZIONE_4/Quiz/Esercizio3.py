'''Esercizio 3'''
def rounded_average(numbers:list[int]) -> int:
    media = sum(numbers) / len(numbers)
    return round(media)

lista = rounded_average([1, 1, 2, 2])
print(lista)
