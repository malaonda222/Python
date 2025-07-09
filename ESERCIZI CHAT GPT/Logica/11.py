def trova_intruso(lista_numeri: list[int]) -> int:
    for i in lista_numeri:
        count = lista_numeri.count(i)
        if count == 1:
            return i 
    
lista = [4, 1, 2, 1, 2, 4, 7]
print(trova_intruso(lista))
