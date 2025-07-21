'''Scrivi una funzione ricorsiva che conti quanti numeri dispari sono presenti
in una data lista.'''



def conta_dispari(lst: list[int]) -> int:
    if len(lst) == 0:
        return 0
    if lst[0] % 2 != 0:
        return 1 + conta_dispari(lst[1:])
    else:
        return conta_dispari(lst[1:])

print(conta_dispari([1, 5, 6, 9, 11, 23]))