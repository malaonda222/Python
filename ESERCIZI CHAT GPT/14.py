def trova_mancante(lista_numeri: list[int], n: int) -> int:  
    somma_numeri = n * (n + 1) // 2
    somma_lista_numeri = sum(lista_numeri)
    risultato = somma_numeri - somma_lista_numeri
    return risultato 

lista1 = ([1, 2, 4, 5])
print(trova_mancante(lista1, 5))
