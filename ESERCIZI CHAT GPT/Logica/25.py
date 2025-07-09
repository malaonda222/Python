def trova_mancante(lista: list[int]) -> int:
    inizio = lista[0]
    fine = lista[-1]
    n = fine - inizio + 1
    somma_attesa = (inizio + fine) * n // 2
    somma_concreta = sum(lista)
    return somma_attesa - somma_concreta

print(trova_mancante(lista = [10, 11, 12, 14, 15]))