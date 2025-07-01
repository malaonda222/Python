'''Esercizio 8'''
def count_isolated(numeri: list[int]) -> int:
    count_isolati = 0
    
    for i in range(len(numeri)):
        
        if (i == 0 or numeri[i] != numeri[i-1]) and (i == len(numeri) -1 or numeri[i] != numeri[i+1]):
            count_isolati += 1
    return count_isolati

lista1 = (count_isolated([1, 2, 2, 3, 3, 3, 4]))
print(lista1)



''''conteggiare i numeri che si ripetono'''
def numeri_ripetuti(numbers: list[int]) -> int:
    conteggio = {}
    for item in numbers:
        if item in conteggio:
            conteggio[item] += 1
        else:
            conteggio[item] = 1
    
    ripetuti = {key: value for key, value in conteggio.items() if value > 1}
    return ripetuti



my_list = (numeri_ripetuti([1, 2, 2, 3, 3, 3, 4]))
print(my_list)