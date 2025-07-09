def somma_pari(lista_interi: list[int]) -> int:
    somma = 0
    for i in lista_interi:
        if not isinstance(i, int) or i < 0:
            raise ValueError("Errore. Il numero deve essere intero positivo")
        if i % 2 == 0:
            somma += i 
    return somma

lista1 = [1, 2, 3, 4, 5, 6]
print(somma_pari(lista1))