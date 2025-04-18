def count_isolated(numeri: list[int]) -> int:
    count_isolati = 0
    
    for i in range(len(numeri)):
        
        if (i == 0 or numeri[i] != numeri[i-1]) and (i == len(numeri) -1 or numeri[i] != numeri[i+1]):
            count_isolati += 1
    return count_isolati

lista1 = (count_isolated([1, 2, 2, 3, 3, 3, 4]))
print(lista1)
