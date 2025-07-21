'''Implementa la ricerca binaria in modo ricorsivo su una lista ordinata'''

def ricerca_binaria(lst, target, inizio, fine):
    if inizio > fine:
        return -1
    meta = (inizio + fine) // 2
    if lst[meta] == target:
        return meta 
    elif lst[meta] < target:
        return ricerca_binaria(lst, target, meta + 1, fine)
    else:
        return ricerca_binaria(lst, target, inizio, meta - 1)    


lista = sorted([1, 2, 5, 8, 9, 11, 15])
target = 9
indice = ricerca_binaria(lista, target, 0, len(lista) - 1)

print(f"Indice trovato: {indice}")