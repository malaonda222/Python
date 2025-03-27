'''Esercizio 5'''
def calculate_average(numbers: list[int]) -> float:
    if len(numbers) == 0:
        return 0
    else:
        return sum(numbers) / len(numbers)
    
print(calculate_average([1, 2, 3, 4, 50]))