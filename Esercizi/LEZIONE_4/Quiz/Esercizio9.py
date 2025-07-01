'''Esercizio9'''
def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    set_senza_numeri_lista = original_set.difference(elements_to_remove)
    return set_senza_numeri_lista

print(remove_elements({5, 6, 7}, [7, 8, 9]))