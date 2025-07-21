'''Scrivi una funzione ricorsiva conta_elemento(lista, elemento) che conta
quante volte elemento appare nella lista.'''

def conta_elemento(lst: list[int], elemento: int) -> int:
    if len(lst) == 0:
        return 0
    if lst[0] == elemento:
        return 1 + conta_elemento(lst[1:], elemento)
    else:
        return conta_elemento(lst[1:], elemento)

print(conta_elemento([1, 2, 3, 2, 4, 2], 2))



