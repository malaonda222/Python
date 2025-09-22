'''Scrivi una funzione che controlla se una riga di Sudoku (9 numeri) è valida, 
ovvero contiene solo numeri da 1 a 9 senza ripetizioni.'''

def is_valid_row(lista_num: list[int]) -> bool:
    if len(lista_num) != 9:
        return False
    lista_ordinata = sorted(lista_num)
    for i in range(9):
        if lista_ordinata[i] == i + 1:
            continue 
        else:
            return False
    return True

def is_valid_row1(lista_num: list[int]) -> bool:
    if len(lista_num) != 9:
        return False
    return set(lista_num) == set(range(1, 10))



print(is_valid_row([1, 2, 4, 5, 6, 3, 6, 7, 8]))
print(is_valid_row1([1, 2, 4, 5, 6, 3, 6, 7, 8]))
print(is_valid_row([1, 2, 3, 5, 4, 6, 8, 7, 9]))
print(is_valid_row1([1, 2, 3, 5, 4, 6, 8, 7, 9]))



