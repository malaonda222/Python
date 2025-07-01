'''Esercizio 1'''
def find_element(lst: list[int], element: int) -> bool:
    for item in lst:
        if item == element:
            return True
    return False

primo_elemento = find_element([1, 2, 3,], 2)
print(primo_elemento)


