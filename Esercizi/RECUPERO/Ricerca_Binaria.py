def ricerca_binaria(lista: list[int], n: int) -> bool:
    inizio = lista[0]
    fine = len(lista) - 1
    medio = (inizio + fine) // 2
    while inizio <= fine:
        if n == lista[medio]:
            return True
        if n > lista[medio]:
            inizio = medio + 1
        else:
            fine = medio - 1
    return False
        

