def primo_negativo(lista: list[int]) -> int:
    for i in range(len(lista)):
        if lista[i] < 0:
            return i
        
    return -1
        
print(primo_negativo([4, 6, -3, 2, -1]))
