'''Ordina una lista di tuple per il secondo elemento.'''

lista_tuple = [(1, 3), (3, 4,), (6, 7)]
def ordina_tuple(lista: tuple[int, int]) -> list[tuple]:
    return sorted(lista, key=lambda item: item[1], reverse=True)

print(ordina_tuple(lista_tuple))