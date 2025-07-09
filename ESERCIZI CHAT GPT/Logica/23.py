def trova_massimo(lista: list) -> int:
    max_num = 0
    for i in range(len(lista)):
        if i == 0:
            max_num = lista[i]
        if lista[i] > max_num:
            max_num = lista[i]
    return max_num

print(trova_massimo([3, 7, 2, 9, 4]))