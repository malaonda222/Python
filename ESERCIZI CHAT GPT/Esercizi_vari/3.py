# '''Scrivi una funzione che somma i numeri che hanno indice pari. 
# Ti viene fornita questa lista:  [5, 8, 12, 7, 3, 10]'''

# def somma_numeri(lista_num: list[int]) -> int:
#     somma = 0
#     for i in range(len(lista_num)):
#         if i % 2 == 0:
#             somma += lista_num[i]
#     return somma 


# print(somma_numeri([5, 8, 12, 7, 3, 10]))

# #list comprehension

# def sum_numeri(lista: list[int]) -> int:
#     return sum([lista[i] for i in range(len(lista)) if i % 2 == 0])


# print(sum_numeri([5, 8, 12, 7, 3, 10]))




'''Scrivi una funzione che riceve una lista di numeri e restituisce la somma 
dei numeri che si trovano in posizione multipla di 3 (quindi indice 0, 3, 6, 9...).'''

def somma_indici_multipli3(lista1: list[int]) -> int:
    somma = 0
    for i in range(len(lista1)):
        if i % 3 == 0:
            somma += lista1[i] 
    return somma


# list comprehension

def som_ind_mul3(lista2: list[int]) -> int:
    return sum([lista2[i] for i in range(len(lista2)) if i % 3 == 0])


print(somma_indici_multipli3([3, 5, 7, 88, 6, 444, 55, 443, 22, 56, 4, 7, 33, 4, 79786, 8]))
print(som_ind_mul3([3, 5, 7, 88, 6, 444, 55, 443, 22, 56, 4, 7, 33, 4, 79786, 8]))
