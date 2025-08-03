'''Inverti una tupla.'''

# def inverti_tuple(tupla: tuple[str, int]) -> tuple:
#     new_tuple = tupla[::-1]
#     return new_tuple

# print(inverti_tuple(("ciao", 6)))


def inverti_tuple(tupla: tuple[int, int]) -> tuple:
    new_tupla = ()
    for element in range(len(tupla)-1, -1, -1):
        new_tupla += (tupla[element],)
    return new_tupla

print(inverti_tuple((8, 6)))
    


# def inverti_lista(lista_numeri: list[int]) -> list:
#     new_list = lista_numeri[::-1]
#     return new_list

# print(inverti_lista([3, 7, 6, 7]))

def inverti_lista(lista_numeri: list[int|str|float|bool]) -> list:
    new_list = []
    for i in range(len(lista_numeri)-1, -1, -1):
        new_list.append(lista_numeri[i])
    return new_list

print(inverti_lista([3, 4, "ciao", "come", True, 7]))


def inverti_lista(lista_numeri: list[int|str|float|bool]) -> list:
    return [lista_numeri[i] for i in range(len(lista_numeri)-1, -1, -1)]

print(inverti_lista([3, 10, "tutto", "come", True, 6.9]))